# Generated by Django 3.2.8 on 2023-08-19 17:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('setting', '0002_alter_type_contract_name'),
        ('user', '0007_auto_20230819_1158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='municipalities',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='setting.municipalities'),
        ),
    ]
