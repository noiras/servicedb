from django.db import models

# Create your models here.
class MasterTable(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ValueTable(models.Model):
    value = models.TextField()
    
class ColumnTable(models.Model):
    INTEGER = 0
    STRING = 1
    DECIMAL = 2
    BOOLEAN = 3
    FILE = 4
    DATE = 5
    TYPE_CHOICES = (        
        (INTEGER, 'Integer'),
        (STRING, 'String'),
        (DECIMAL, 'Decimal'),
        (BOOLEAN, 'Boolean'),
        (FILE, 'File'),
        (DATE, 'Date')
    )

    master_table = models.ForeignKey(MasterTable, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    data_type = models.SmallIntegerField(choices=TYPE_CHOICES)
    value = models.ManyToManyField(ValueTable)

    def __str__(self):
        return f'{self.name} {self.get_data_type_display()}'