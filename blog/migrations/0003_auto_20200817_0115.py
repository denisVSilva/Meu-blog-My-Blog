# Generated by Django 3.1 on 2020-08-17 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200817_0114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pythonprojects',
            name='Descrição',
            field=models.TextField(max_length=250),
        ),
    ]
