# Generated by Django 4.1.1 on 2022-11-28 07:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spapp', '0002_album_delete_postimage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='album',
            old_name='image',
            new_name='album',
        ),
    ]