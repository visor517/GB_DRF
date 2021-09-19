import json

from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient, APISimpleTestCase, APITestCase
# from mixer.backend.django import mixer
from django.contrib.auth.models import User

from todos.models import Project
from todos.views import ProjectsViewSet
from users.views import UsersViewSet
from users.models import User


class TestAuthorViewSet(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            'user_test', 'user_test@test.ts', 'geekbrains'
        )
        self.super_user = get_user_model().objects.create_superuser(
            'django', 'user_admin_test@test.ts', 'geekbrains'
        )

    def test_get_list_guest(self):
        print('\n===> TEST 1.1 test_get_list_guest')
        factory = APIRequestFactory()
        request = factory.get('/api/users/')
        view = UsersViewSet.as_view({'get': 'list'})
        response = view(request)
        response.render()
        print(response.content)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_list(self):
        print('\n===> TEST 1.2 test_get_list')
        factory = APIRequestFactory()
        request = factory.get('/api/users/')
        force_authenticate(request, user=self.user)
        view = UsersViewSet.as_view({'get': 'list'})
        response = view(request)
        response.render()
        print(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_project_superuser(self):
        print('\n===> TEST 1.3 test_create_project')
        factory = APIRequestFactory()
        request = factory.post('/api/projects/', {'name': 'Test project',
                                                  'description': 'Test description',
                                                  'authors': [self.super_user.pk]}, format='json')
        force_authenticate(request, user=self.super_user)
        view = ProjectsViewSet.as_view({'post': 'create'})
        response = view(request)
        response.render()
        print(response.content)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # APIClient
    def test_get_project_guest(self):
        print('\n===> TEST 2.1 test_get_project_guest')
        project = Project.objects.create(name='Test 4',
                                         description='Test description')
        client = APIClient()
        response = client.get(f'/api/projects/{project.id}/')
        print(response.content)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_project_user(self):
        print('\n===> TEST 2.2 test_get_project_user')
        project = Project.objects.create(name='Test 4',
                                         description='Test description')
        client = APIClient()
        client.force_authenticate(user=self.user)
        response = client.get(f'/api/projects/{project.id}/')
        print(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
