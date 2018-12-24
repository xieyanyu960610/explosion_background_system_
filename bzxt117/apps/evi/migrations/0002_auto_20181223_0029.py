# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-22 16:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deveviftirtestfile',
            name='txtHandledURL',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='处理过的TXT文档路径'),
        ),
        migrations.AlterField(
            model_name='deveviramantestfile',
            name='txtHandledURL',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='处理过的TXT文档路径'),
        ),
        migrations.AlterField(
            model_name='devevixrftestfile',
            name='handledURL',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='有效元素列表'),
        ),
        migrations.AlterField(
            model_name='exploeviftirtestfile',
            name='txtHandledURL',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='处理过的TXT文档路径'),
        ),
        migrations.AlterField(
            model_name='exploevigcmsfile',
            name='txtHandledURL',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='处理过的TXT文档路径'),
        ),
        migrations.AlterField(
            model_name='exploeviramantestfile',
            name='txtHandledURL',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='处理过的TXT文档路径'),
        ),
        migrations.AlterField(
            model_name='exploevixrdtestfile',
            name='txtHandledURL',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='处理过的TXT文档路径'),
        ),
        migrations.AlterField(
            model_name='exploevixrftestfile',
            name='handledURL',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='有效元素列表'),
        ),
    ]