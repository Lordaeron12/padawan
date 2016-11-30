# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-30 22:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_remove_productpicture_embed_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
            ],
        ),
        migrations.RenameField(
            model_name='variant',
            old_name='stock',
            new_name='stock_quantity',
        ),
        migrations.RenameField(
            model_name='variant',
            old_name='name',
            new_name='value',
        ),
        migrations.AddField(
            model_name='variant',
            name='feature',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.Feature'),
        ),
    ]