# Generated by Django 2.2.18 on 2021-02-13 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_entry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='text',
            field=models.TextField(max_length=200),
        ),
    ]
