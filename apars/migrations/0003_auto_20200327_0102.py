# Generated by Django 2.2.4 on 2020-03-26 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apars', '0002_auto_20200327_0028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='currency',
            field=models.TextField(blank=True, null=True, verbose_name='Валюта'),
        ),
    ]
