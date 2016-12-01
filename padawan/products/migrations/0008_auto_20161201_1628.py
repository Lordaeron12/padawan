# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-01 21:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0015_fill_filter_spec_field'),
        ('products', '0007_auto_20161201_1618'),
    ]

    operations = [
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
        ),
        migrations.AlterModelOptions(
            name='feature',
            options={'verbose_name': 'Caracter\xedstica', 'verbose_name_plural': 'Caracter\xedsticas'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Producto', 'verbose_name_plural': 'Productos'},
        ),
        migrations.RemoveField(
            model_name='productpicture',
            name='id',
        ),
        migrations.RemoveField(
            model_name='productpicture',
            name='image',
        ),
        migrations.AddField(
            model_name='productpicture',
            name='picture_ptr',
            field=models.OneToOneField(auto_created=True, default=1, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='products.Picture'),
            preserve_default=False,
        ),
    ]
