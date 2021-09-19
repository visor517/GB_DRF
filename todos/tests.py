import json
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient, APISimpleTestCase, APITestCase
# from mixer.backend.django import mixer
from django.contrib.auth.models import User
from users.views import UsersViewSet
from users.models import User


class TestAuthorViewSet(TestCase):

    def test_get_list(self):
        factory = APIRequestFactory()
        request = factory.get('/api/users/')
        view = UsersViewSet.as_view({'get': 'list'})
        response = view(request)
        response.render()
        print(response.content)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
