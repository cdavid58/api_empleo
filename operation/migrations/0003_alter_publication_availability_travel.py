# Generated by Django 3.2.8 on 2023-08-11 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0002_auto_20230811_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='availability_travel',
            field=models.BooleanField(default=True),
        ),
    ]