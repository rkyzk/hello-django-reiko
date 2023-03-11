from django.test import TestCase
from .models import Item


class TestModels(TestCase):

    def test_done_defaults_to_false(self):
        """test our item is created with done status = false by default"""
        item = Item.objects.create(name='Test todo Item')
        self.assertFalse(item.done)

    def test_item_string_method_returns_name(self):
        item = Item.objects.create(name='Test todo Item')
        self.assertEqual(str(item), 'Test todo Item')
