# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-13 14:23
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sm_goods', '0004_auto_20180812_2249'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activitygoods',
            name='goodssku',
        ),
        migrations.AddField(
            model_name='activitygoods',
            name='goodssku',
            field=models.ManyToManyField(to='sm_goods.GoodsSKU', verbose_name='商品SKU ID'),
        ),
        migrations.AlterField(
            model_name='goodsspu',
            name='SPUdetail',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='商品详情'),
        ),
    ]