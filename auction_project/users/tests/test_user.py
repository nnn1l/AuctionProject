from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.conf import settings
from items.factories import ItemFactory, CategoryFactory
from .factories import UserFactory

User = get_user_model()


class UserViewsTestCase(TestCase):
    def setUp(self):
        self.user = UserFactory(password='password')
        self.user.set_password('password')
        self.user.save()
        self.client.login(username=self.user.username, password='password')

        self.other_user = UserFactory()

        self.category = CategoryFactory()
        self.item = ItemFactory(owner=self.user, category=self.category)
        self.other_item = ItemFactory(owner=self.other_user, category=self.category)

    def test_user_register_view_post(self):
        """  Tests registration view post """
        self.client.logout()
        url = reverse('user-register')
        data = {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'first_name': 'New',
            'last_name': 'User',
            'password1': 'ComplexPass123!',
            'password2': 'ComplexPass123!',
        }
        response = self.client.post(url, data)
        if response.status_code == 200:
            print(response.context['form'].errors)  # shows errors
        self.assertEqual(response.status_code, 302)  # redirect
        self.assertTrue(User.objects.filter(username='newuser').exists())

    def test_user_login_view_get(self):
        """  Tests login view get  """
        self.client.logout()
        url = reverse('user-login')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_user_login_view_post(self):
        """  Tests login view post  """
        self.client.logout()
        url = reverse('user-login')
        data = {
            'username': self.user.username,
            'password': 'password'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)  # redirect after logining
        self.assertEqual(response.url, reverse('all-categories'))

    def test_user_profile_view(self):
        """  Tests user profile view  """
        url = reverse('user-profile', kwargs={'pk': self.user.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile-detail.html')
        self.assertContains(response, self.user.username)

    def test_user_update_profile_view_get(self):
        """  Tests updating profile get view  """
        url = reverse('user-edit', kwargs={'pk': self.user.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile-update.html')

    def test_user_update_profile_view_post(self):
        """  Tests updating info profile  """
        url = reverse('user-edit', kwargs={'pk': self.user.pk})
        data = {
            'first_name': 'Updated',
            'last_name': 'Name',
            'username': 'updateduser',
            'biography': 'Updated biography',
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302) # redirect
        self.user.refresh_from_db() # updating db
        self.assertEqual(self.user.username, 'updateduser')
        self.assertEqual(self.user.first_name, 'Updated')

    def test_users_items_list_view(self):
        """  Tests user`s item list view  """
        url = reverse('user-items', kwargs={'pk': self.user.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user-items.html')
        items = response.context['items']  # all user`s items
        self.assertIn(self.item, items)  # user`s item == user`s items - > OK
        self.assertNotIn(self.other_item, items)  # not user`s item != user`s item - > OK

    def test_login_required_views_redirect(self):
        """  Tests if login require works correctly  """
        self.client.logout()
        urls = [
            reverse('user-edit', kwargs={'pk': self.user.pk}),
            reverse('user-items', kwargs={'pk': self.user.pk}),
        ]
        for url in urls:
            response = self.client.get(url)
            self.assertRedirects(response, f'{settings.LOGIN_URL}?next={url}')



