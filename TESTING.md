<h1 id="top">Tatted Backend API Testing</h1>

back to the [README.md](README.md)

## Contents
-   [Automated Unit Testing](#unit-testing)
    -   [Profiles Views](#profiles-views)
    -   [Posts Views](#posts-views)
    -   [Comments Views](#comments-views)
    -   [Review Views](#reviews-views)
-  [Manual Testing](#manual-testing)
    -   [API Endpoint Tests](#api-endpoint-tests)
    -   [CRUD Testing](#crud-testing)
-  [Validator Testing](#pycodestyle-validator-testing)
-  [Bugs](#bugs)

<h2 id="unit-testing">Automated Unit Testing</h2>

The APITestCase functionality from DRF was utilized to perform automated testing on all model instances in the API itself.

<br />

<h3 id="profiles-views">Profiles Views</h3>

One test was written to test the retrieval of the profile instances which are created through django signals when a user creates an account.

```
class ProfileListView(APITestCase):
    def setUp(self):
        CustomUser.objects.create_user(
            username='testuser', password='pass', is_artist=False)
        CustomUser.objects.create_user(
            username='testartist', password='pass', is_artist=True)

    def test_can_list_profiles(self):
        response = self.client.get('/profiles/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
```

Four tests were written to test the functionality of the profile detail view:
- To test for the retrieval of a profile model instance by valid pk.
- To test for the failure to retrieve of a profile model instance by invalid pk.
- To test that a user can update the profile model instance if 'is_owner' = True.
- To test that a user cannot update the profile model instance if 'is_owner' = False.

```
class ProfileDetailView(APITestCase):
    def setUp(self):
        CustomUser.objects.create_user(
            username='testuser', password='pass', is_artist=False)
        CustomUser.objects.create_user(
            username='testartist', password='pass', is_artist=True)

    def test_can_retrieve_profile_using_valid_id(self):
        response = self.client.get('/profiles/1/')
        self.assertEqual(response.data['owner'], 'testuser')
        response2 = self.client.get('/profiles/2/')
        self.assertEqual(response2.data['owner'], 'testartist')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cant_retrieve_profile_using_invalid_id(self):
        response = self.client.get('/profiles/3/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_update_their_own_profile(self):
        self.client.login(username='testuser', password='pass')
        response = self.client.put(
            '/profiles/1/', {'name': 'testtatter'})
        profile = Profile.objects.filter(pk=1).first()
        self.assertEqual(profile.name, 'testtatter')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cannot_update_another_users_profile(self):
        self.client.login(username='testuser', password='pass')
        response = self.client.put(
            '/profiles/2/', {'name': 'testtatter'})
        profile = Profile.objects.filter(pk=1).first()
        self.assertEqual(profile.name, '')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
```

The coverage report for this automated unit testing was as follows:

![Coverage Report Profiles View](/docs/screenshots/coverage-profiles.png)


<a href="#top">Back to the top.</a>

<h3 id="posts-views">Posts Views</h3>

Three tests were written to test the functionality of the post list view:
- To test the retrieval of all post model instances
- To test that users can create a post instance if 'is_artist' is True.
- To test that users cannot create a post instance if 'is_artist' is False.

```
class PostListViewTests(APITestCase):
    def setUp(self):
        CustomUser.objects.create_user(
            username='testuser', password='pass', is_artist=False)
        CustomUser.objects.create_user(
            username='testartist', password='pass', is_artist=True)

    def test_can_list_posts(self):
        testuser1 = CustomUser.objects.get(username='testuser')
        Post.objects.create(owner=testuser1, content='Hey')
        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_only_logged_in_artists_can_create_post(self):
        self.client.login(username='testuser', password='pass')
        response = self.client.post(
            '/posts/', {'content': 'testing non artist can post'})
        count = Post.objects.count()
        self.assertEqual(count, 0)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.client.login(username='testartist', password='pass')
        response = self.client.post(
            '/posts/', {'content': 'testing non artist can post'})
        count = Post.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_users_not_logged_in_cannot_create_posts(self):
        response = self.client.post(
            '/posts/',
            {'content': 'testing if unauthenticated users can post'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
```

Four tests were written to test the functionality of the post detail view:
- To test that a post instance will be returned when referencing a valid pk.
- To test that a post instance will not be returned when referencing an invalid pk.
- To test that a user can update a post instance if 'is_owner' = True.
- To test that a user cannot update a post instance if 'is_owner' = False.

```
class PostDetailViewTests(APITestCase):
    def setUp(self):
        nonartist = CustomUser.objects.create_user(
            username='testuser', password='pass', is_artist=False)
        artist = CustomUser.objects.create_user(
            username='testartist', password='pass', is_artist=True)
        Post.objects.create(
            owner=artist, content='test post by artist'
        )

    def test_can_retrieve_post_using_valid_id(self):
        response = self.client.get('/posts/1/')
        self.assertEqual(response.data['content'], 'test post by artist')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cant_retrieve_post_using_invalid_id(self):
        response = self.client.get('/posts/2/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_artist_can_update_their_own_posts(self):
        self.client.login(username='testartist', password='pass')
        response = self.client.put(
            '/posts/1/', {'content': 'test updating content'})
        post = Post.objects.filter(pk=1).first()
        self.assertEqual(post.content, 'test updating content')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_only_owner_can_update_the_post(self):
        self.client.login(username='testuser', password='pass')
        response = self.client.put(
            '/posts/1/', {'content': 'This is not allowed for me to do'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
```

The coverage report for this automated unit testing was as follows:

![Coverage Report Posts View](/docs/screenshots/coverage-posts.png)


<a href="#top">Back to the top.</a>

<h3 id="comments-views">Comments Views</h3>

Three tests were written to test the functionality of the comment list view:
- To test the retrieval of all created comment instances.
- To test that authenticated users can create a comment instance.
- To test that unauthenticated users cannot create a comment instance.

```
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
```

Four tests were written to test the functionality of the comment detail view:
- To test the retrieval of a comment instance with reference to a valid pk.
- To test the failure to retrieve a comment instance with reference to an invalid pk.
- To test that users can update a comment instance if 'is_owner' = True.
- To test that users cannot update a comment instance if 'is_owner' = False.

```
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
```

The coverage report for this automated unit testing was as follows:

![Coverage Report Comments View](/docs/screenshots/coverage-comments.png)

<a href="#top">Back to the top.</a>

<h3 id="reviews-views">Reviews Views</h3>

Three tests were written to test the functionality of the review list view:
- To test the retrieval of all created review instances.
- To test that authenticated users can create a review instance.
- To test that unauthenticated users cannot create a review instance.

```
class ReviewListTests(APITestCase):
    def setUp(self):
        CustomUser.objects.create_user(
            username='testuser', password='pass', is_artist=False)
        CustomUser.objects.create_user(
            username='testartist', password='pass', is_artist=True)

    def test_can_list_reviews(self):
        response = self.client.get('/reviews/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_in_users_can_create_reviews(self):
        self.client.login(username='testuser', password='pass')
        response = self.client.post(
            '/reviews/',
            {
                'artist': 2,
                'content': 'I was happy with this experience',
                'satisfaction_rating': 'highly recommends'
            }
        )
        count = Review.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_unauthenticated_users_cannot_create_reviews(self):
        response = self.client.post(
            '/reviews/',
            {
                'artist': 2,
                'content': 'I was happy with this experience',
                'satisfaction_rating': 'highly recommends'
            }
        )
        count = Review.objects.count()
        self.assertEqual(count, 0)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
```

Four tests were written to test the functionality of the review detail view:
- To test the retrieval of a specified review instance with reference to a valid pk.
- To test the failure of retrieving a specified review instance with reference to an invalid pk.
- To test that a user can update a review instance if 'is_owner' = True.
- To test that a user cannot update a review instance if 'is_owner' = False.

```
class ReviewDetailTests(APITestCase):
    def setUp(self):
        testuser = CustomUser.objects.create_user(
            username='testuser', password='pass', is_artist=False)
        testartist = CustomUser.objects.create_user(
            username='testartist', password='pass', is_artist=True)
        Review.objects.create(
            owner=testuser,
            artist=testartist,
            content='review content',
            satisfaction_rating='highly recommends'
        )

    def test_can_retrieve_review_using_valid_id(self):
        response = self.client.get('/reviews/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cant_retrieve_review_using_invalid_id(self):
        response = self.client.get('/reviews/2/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_owner_can_update_the_review(self):
        self.client.login(username='testuser', password='pass')
        response = self.client.put(
            '/reviews/1/', {'content': 'updated review content',
                            'satisfaction_rating': 'somewhat recommends'})
        review = Review.objects.filter(pk=1).first()
        self.assertEqual(review.content, 'updated review content')
        self.assertEqual(review.satisfaction_rating, 'somewhat recommends')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_users_who_are_not_owner_cannot_update_the_review(self):
        self.client.login(username='testartist', password='pass')
        response = self.client.put(
            '/reviews/1/', {'content': 'updated review content',
                            'satisfaction_rating': 'somewhat recommends'})
        review = Review.objects.filter(pk=1).first()
        self.assertEqual(review.content, 'review content')
        self.assertEqual(review.satisfaction_rating, 'highly recommends')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
```

The coverage report for this automated unit testing was as follows:

![Coverage Report Reviews Views](/docs/screenshots/coverage-reviews.png)

<a href="#top">Back to the top.</a>