from .models import Post
from users.models import CustomUser
from rest_framework import status
from rest_framework.test import APITestCase


# class PostListViewTests(APITestCase):
#     def setUp(self):
#         CustomUser.objects.create_user(
#             username='testuser', password='pass', is_artist=False)
#         CustomUser.objects.create_user(
#             username='testartist', password='pass', is_artist=True)

#     def test_can_list_posts(self):
#         testuser1 = CustomUser.objects.get(username='testuser')
#         Post.objects.create(owner=testuser1, content='Hey')
#         response = self.client.get('/posts/')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#     def test_only_logged_in_artists_can_create_post(self):
#         self.client.login(username='testuser', password='pass')
#         response = self.client.post(
#             '/posts/', {'content': 'testing non artist can post'})
#         count = Post.objects.count()
#         self.assertEqual(count, 0)
#         self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
#         self.client.login(username='testartist', password='pass')
#         response = self.client.post(
#             '/posts/', {'content': 'testing non artist can post'})
#         count = Post.objects.count()
#         self.assertEqual(count, 1)
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)

#     def test_users_not_logged_in_cannot_create_posts(self):
#         response = self.client.post(
#             '/posts/',
#             {'content': 'testing if unauthenticated users can post'})
#         self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


# class PostDetailViewTests(APITestCase):
#     def setUp(self):
#         nonartist = CustomUser.objects.create_user(
#             username='testuser', password='pass', is_artist=False)
#         artist = CustomUser.objects.create_user(
#             username='testartist', password='pass', is_artist=True)
#         Post.objects.create(
#             owner=artist, content='test post by artist'
#         )

#     def test_can_retrieve_post_using_valid_id(self):
#         response = self.client.get('/posts/1/')
#         self.assertEqual(response.data['content'], 'test post by artist')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#     def test_cant_retrieve_post_using_invalid_id(self):
#         response = self.client.get('/posts/2/')
#         self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

#     def test_artist_can_update_their_own_posts(self):
#         self.client.login(username='testartist', password='pass')
#         response = self.client.put(
#             '/posts/1/', {'content': 'test updating content'})
#         post = Post.objects.filter(pk=1).first()
#         self.assertEqual(post.content, 'test updating content')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#     def test_only_owner_can_update_the_post(self):
#         self.client.login(username='testuser', password='pass')
#         response = self.client.put(
#             '/posts/1/', {'content': 'This is not allowed for me to do'})
#         self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
