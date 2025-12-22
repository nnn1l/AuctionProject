from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.conf import settings
from .models import Item
from .factories import CategoryFactory, ItemFactory
from users.factories import UserFactory

User = get_user_model()


class ItemViewsTestCase(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.client.force_login(self.user)
        self.category = CategoryFactory()
        self.item = ItemFactory(owner=self.user, category=self.category)

    def test_item_create_view_get(self):
        url = reverse('item-create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'item_template/item-create.html')

    def test_item_create_view_post(self):
        url = reverse('item-create')
        data = {
            'title': 'New Item',
            'category': self.category.id,
            'description': 'Item description',
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)  # редірект після створення
        item = Item.objects.get(title='New Item')
        self.assertEqual(item.owner, self.user)

    def test_item_detail_view(self):
        url = reverse('item-details', kwargs={'pk': self.item.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.item.title)
        self.assertTemplateUsed(response, 'item_template/item-details.html')

    def test_item_update_view_get(self):
        url = reverse('item-update', kwargs={'pk': self.item.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'item_template/item-update.html')

    def test_item_update_view_post(self):
        url = reverse('item-update', kwargs={'pk': self.item.pk})
        data = {
            'title': 'Updated Title',
            'category': self.category.id,
            'description': 'Updated description',
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)
        self.item.refresh_from_db()
        self.assertEqual(self.item.title, 'Updated Title')

    def test_item_delete_view_get(self):
        url = reverse('item-delete', kwargs={'pk': self.item.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'item_template/item-delete.html')

    def test_item_delete_view_post(self):
        url = reverse('item-delete', kwargs={'pk': self.item.pk})
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        with self.assertRaises(Item.DoesNotExist):
            Item.objects.get(pk=self.item.pk)

    def test_login_required_redirect(self):
        self.client.logout()
        urls = [
            reverse('item-create'),
            reverse('item-details', kwargs={'pk': self.item.pk}),
            reverse('item-update', kwargs={'pk': self.item.pk}),
        ]
        for url in urls:
            response = self.client.get(url)
            self.assertRedirects(response, f'{settings.LOGIN_URL}?next={url}')




# Create your tests here.
