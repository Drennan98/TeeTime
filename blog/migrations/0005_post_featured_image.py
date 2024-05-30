# Generated by Django 5.0.6 on 2024-05-28 17:09

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_comment_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='featured_image',
            field=cloudinary.models.CloudinaryField(default='add placeholder text...', max_length=255, verbose_name='#'),
        ),
    ]