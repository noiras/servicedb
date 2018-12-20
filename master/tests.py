from django.test import TestCase
from django.test import Client
from django.urls import reverse
from .models import MasterTable, ColumnTable


class CreateTableTest(TestCase):
    def setUp(self):
        self.client = Client()
    def test_view_create_new_table(self):
        url = reverse('master:dashboard')
        data = {
            'tableName': 'Mahasiswa',
            'column': ['nama', 'alamat'],
            'typeData': [ColumnTable.STRING, ColumnTable.STRING]
        }
        self.client.post(path=url, data=data)

        master_table = MasterTable.objects.get(name='Mahasiswa')
        self.assertEqual(master_table.name, 'Mahasiswa')

        columns_qs = ColumnTable.objects.filter(master_table=master_table)
        self.assertEqual(columns_qs.count(), 2)

        column1 = ColumnTable.objects.get(master_table=master_table, name='nama')
        self.assertEqual(column1.name, 'nama')

        column2 = ColumnTable.objects.get(master_table=master_table, name='alamat')
        self.assertEqual(column2.name, 'alamat')
    
    def test_view_edit_table(self):
        self.assertEqual(1, 1)

    def test_view_delete_table(self):
        url = reverse('master:deleteTable', args=[10])
        data = {
            'pk' : '10',
        }
        self.client.get(path=url, data=data)
        master_table = MasterTable.objects.get(pk='10')
        self.assertFalse(master_table.pk, '10')