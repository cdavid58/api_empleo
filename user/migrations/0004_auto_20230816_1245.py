# Generated by Django 3.2.8 on 2023-08-16 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_user_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='photo_cover',
            field=models.ImageField(blank=True, null=True, upload_to='Cover_User'),
        ),
        migrations.AddField(
            model_name='user',
            name='photo_profile',
            field=models.ImageField(blank=True, null=True, upload_to='Profile_User'),
        ),
    ]
