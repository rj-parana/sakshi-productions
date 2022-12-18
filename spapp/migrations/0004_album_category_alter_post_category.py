# Generated by Django 4.1.1 on 2022-12-01 09:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('spapp', '0003_rename_image_album_album'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='album_category', to='spapp.category'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_category', to='spapp.category'),
        ),
    ]