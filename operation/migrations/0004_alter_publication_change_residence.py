# Generated by Django 3.2.8 on 2023-08-11 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0003_alter_publication_availability_travel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='change_residence',
            field=models.BooleanField(default=True),
        ),
    ]
