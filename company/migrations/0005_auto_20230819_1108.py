# Generated by Django 3.2.8 on 2023-08-19 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0004_alter_company_phone_2'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='password',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='type_user',
            field=models.IntegerField(default=2),
        ),
    ]
