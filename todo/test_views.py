from django.test import TestCase
from .models import Item

#why not test can edit and can add?
class TestViews(TestCase):

    def test_get_todo_list(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/todo_list.html')

    def test_get_add_item_page(self):
        response = self.client.get('/add')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/add_item.html')

    def test_get_edit_item_page(self):
        item = Item.objects.create(name='test Todo item')
        response = self.client.get(f'/edit/{item.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/edit_item.html')


    def test_can_add_item_(self):
        response = self.client.post('/add', {'name': 'Test added item'})
        self.assertRedirects(response, '/')

    
    def test_can_delete_item_(self):
        item = Item.objects.create(name='test Todo item')
        response = self.client.get(f'/delete/{item.id}')
        self.assertRedirects(response, '/')
        existing_items = Item.objects.filter(id=item.id)
        self.assertEqual(len(existing_items), 0)
    
    def test_can_toggle_item_(self):
        item = Item.objects.create(name='test Todo item', done=True)
        response = self.client.get(f'/toggle/{item.id}')
        self.assertRedirects(response, '/')
        updated_item = Item.objects.get(id=item.id)
        self.assertFalse(updated_item.done, 'done')

    def test_can_edit_item(self):
        item = Item.objects.create(name='test Todo item')
        response = self.client.post(f'/edit/{item.id}', {'name': 'Updated name'})
        self.assertRedirects(response, '/')
        updated_item = Item.objects.get(id=item.id)
        self.assertEqual(updated_item.name, 'Updated name')


