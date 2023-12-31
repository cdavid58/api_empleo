# Generated by Django 3.2.8 on 2023-08-16 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20230816_1245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='photo_cover',
            field=models.ImageField(blank=True, default='Cover_User/without_logo.png', null=True, upload_to='Cover_User'),
        ),
        migrations.AlterField(
            model_name='user',
            name='photo_profile',
            field=models.ImageField(blank=True, default='Profile_User/without_logo.png', null=True, upload_to='Profile_User'),
        ),
    ]
