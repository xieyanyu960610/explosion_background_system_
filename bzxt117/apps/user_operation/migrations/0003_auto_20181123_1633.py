# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-23 08:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_operation', '0002_usermessage_hashandle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allowupdate',
            name='devEviId',
            field=models.IntegerField(blank=True, null=True, verbose_name='所涉及的爆炸装置物证'),
        ),
        migrations.AlterField(
            model_name='usermessage',
            name='devEviId',
            field=models.IntegerField(blank=True, null=True, verbose_name='所涉及的爆炸装置物证'),
        ),
    ]