from users.models import CustomUser
from .models import Profile
from rest_framework import status
from rest_framework.test import APITestCase


# class ProfileListView(APITestCase):
#     def setUp(self):
#         CustomUser.objects.create_user(
#             username='testuser', password='pass', is_artist=False)
#         CustomUser.objects.create_user(
#             username='testartist', password='pass', is_artist=True)

#     def test_can_list_profiles(self):
#         response = self.client.get('/profiles/')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)


# class ProfileDetailView(APITestCase):
#     def setUp(self):
#         CustomUser.objects.create_user(
#             username='testuser', password='pass', is_artist=False)
#         CustomUser.objects.create_user(
#             username='testartist', password='pass', is_artist=True)

#     def test_can_retrieve_profile_using_valid_id(self):
#         response = self.client.get('/profiles/1/')
#         self.assertEqual(response.data['owner'], 'testuser')
#         response2 = self.client.get('/profiles/2/')
#         self.assertEqual(response2.data['owner'], 'testartist')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#     def test_cant_retrieve_profile_using_invalid_id(self):
#         response = self.client.get('/profiles/3/')
#         self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

#     def test_user_can_update_their_own_profile(self):
#         self.client.login(username='testuser', password='pass')
#         response = self.client.put(
#             '/profiles/1/', {'name': 'testtatter'})
#         profile = Profile.objects.filter(pk=1).first()
#         self.assertEqual(profile.name, 'testtatter')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#     def test_user_cannot_update_another_users_profile(self):
#         self.client.login(username='testuser', password='pass')
#         response = self.client.put(
#             '/profiles/2/', {'name': 'testtatter'})
#         profile = Profile.objects.filter(pk=1).first()
#         self.assertEqual(profile.name, '')
#         self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
