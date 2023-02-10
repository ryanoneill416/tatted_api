from .models import Review
from users.models import CustomUser
from rest_framework import status
from rest_framework.test import APITestCase


# class ReviewListTests(APITestCase):
#     def setUp(self):
#         CustomUser.objects.create_user(
#             username='testuser', password='pass', is_artist=False)
#         CustomUser.objects.create_user(
#             username='testartist', password='pass', is_artist=True)

#     def test_can_list_reviews(self):
#         response = self.client.get('/reviews/')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#     def test_logged_in_users_can_create_reviews(self):
#         self.client.login(username='testuser', password='pass')
#         response = self.client.post(
#             '/reviews/',
#             {
#                 'artist': 2,
#                 'content': 'I was happy with this experience',
#                 'satisfaction_rating': 'highly recommends'
#             }
#         )
#         count = Review.objects.count()
#         self.assertEqual(count, 1)
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)

#     def test_unauthenticated_users_cannot_create_reviews(self):
#         response = self.client.post(
#             '/reviews/',
#             {
#                 'artist': 2,
#                 'content': 'I was happy with this experience',
#                 'satisfaction_rating': 'highly recommends'
#             }
#         )
#         count = Review.objects.count()
#         self.assertEqual(count, 0)
#         self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


# class ReviewDetailTests(APITestCase):
#     def setUp(self):
#         testuser = CustomUser.objects.create_user(
#             username='testuser', password='pass', is_artist=False)
#         testartist = CustomUser.objects.create_user(
#             username='testartist', password='pass', is_artist=True)
#         Review.objects.create(
#             owner=testuser,
#             artist=testartist,
#             content='review content',
#             satisfaction_rating='highly recommends'
#         )

#     def test_can_retrieve_review_using_valid_id(self):
#         response = self.client.get('/reviews/1/')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#     def test_cant_retrieve_review_using_invalid_id(self):
#         response = self.client.get('/reviews/2/')
#         self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

#     def test_owner_can_update_the_review(self):
#         self.client.login(username='testuser', password='pass')
#         response = self.client.put(
#             '/reviews/1/', {'content': 'updated review content',
#                             'satisfaction_rating': 'somewhat recommends'})
#         review = Review.objects.filter(pk=1).first()
#         self.assertEqual(review.content, 'updated review content')
#         self.assertEqual(review.satisfaction_rating, 'somewhat recommends')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#     def test_users_who_are_not_owner_cannot_update_the_review(self):
#         self.client.login(username='testartist', password='pass')
#         response = self.client.put(
#             '/reviews/1/', {'content': 'updated review content',
#                             'satisfaction_rating': 'somewhat recommends'})
#         review = Review.objects.filter(pk=1).first()
#         self.assertEqual(review.content, 'review content')
#         self.assertEqual(review.satisfaction_rating, 'highly recommends')
#         self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
