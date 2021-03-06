# Generated by Django 3.0.6 on 2020-06-05 13:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category_slug',
            field=models.SlugField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.Category'),
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(default='', max_length=200),
        ),
    ]
