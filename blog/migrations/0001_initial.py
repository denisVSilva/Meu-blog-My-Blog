# Generated by Django 3.1 on 2020-08-17 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blenderProjects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Titulo', models.CharField(max_length=100)),
                ('Descrição', models.CharField(max_length=250)),
                ('Link', models.CharField(max_length=250)),
                ('imagen', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='pythonProjects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Titulo', models.CharField(max_length=100)),
                ('Descrição', models.CharField(max_length=250)),
                ('Link', models.CharField(max_length=250)),
            ],
        ),
    ]
