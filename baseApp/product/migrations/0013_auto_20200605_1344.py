# Generated by Django 3.0.6 on 2020-06-05 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0012_auto_20200605_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(default='', max_length=200, unique=True),
        ),
    ]
