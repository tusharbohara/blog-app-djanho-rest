# Generated by Django 3.2.4 on 2021-06-15 20:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='post',
            new_name='posts',
        ),
    ]