# Generated by Django 5.1 on 2024-08-30 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_listmodel_show'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listmodel',
            name='show',
            field=models.BooleanField(default=False),
        ),
    ]
