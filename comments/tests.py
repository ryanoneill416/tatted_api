from .models import Comment
from posts.models import Post
from users.models import CustomUser
from rest_framework import status
from rest_framework.test import APITestCase


class CommentListTests(APITestCase):
    def setUp(self):
        CustomUser.objects.create_user(
            username='testuser', password='pass', is_artist=False)
        CustomUser.objects.create_user(
            username='testartist', password='pass', is_artist=True)
        testartist = CustomUser.objects.get(username='testartist')
        Post.objects.create(owner=testartist, content='test post')

    def test_can_list_comments(self):
        response = self.client.get('/comments/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_in_users_can_create_comments(self):
        self.client.login(username='testuser', password='pass')
        response = self.client.post(
            '/comments/',
            {
                'post': 1,
                'content': 'test comment'
            }
        )
        count = Comment.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_users_not_logged_in_cannot_create_comments(self):
        response = self.client.post(
            '/comments/',
            {
                'post': 1,
                'content': 'test comment'
            }
        )
        count = Comment.objects.count()
        self.assertEqual(count, 0)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class CommentDetailViewTests(APITestCase):
    def setUp(self):
        CustomUser.objects.create_user(
            username='testuser', password='pass', is_artist=False)
        CustomUser.objects.create_user(
            username='testartist', password='pass', is_artist=True)
        testartist = CustomUser.objects.get(username='testartist')
        testuser = CustomUser.objects.get(username='testuser')
        post = Post.objects.create(owner=testartist, content='test post')
        Comment.objects.create(owner=testuser, post=post, content='test comm')

    def test_can_retrieve_comment_using_valid_id(self):
        response = self.client.get('/comments/1/')
        self.assertEqual(response.data['content'], 'test comm')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cant_retrieve_comment_using_invalid_id(self):
        response = self.client.get('/comments/2/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_owner_can_update_their_own_comment(self):
        self.client.login(username='testuser', password='pass')
        response = self.client.put(
            '/comments/1/', {'content': 'test updating content'})
        comment = Comment.objects.filter(pk=1).first()
        self.assertEqual(comment.content, 'test updating content')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_only_owner_can_update_the_comment(self):
        self.client.login(username='testartist', password='pass')
        response = self.client.put(
            '/comments/1/', {'content': 'This is not allowed for me to do'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
