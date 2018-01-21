# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-21 07:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ApplyRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applicant', models.CharField(max_length=256)),
                ('name', models.CharField(max_length=256)),
                ('status', models.SmallIntegerField(choices=[(0, '已申请'), (1, '已审核'), (2, '已完成'), (3, '被否决')], default=0)),
                ('model', models.CharField(max_length=256)),
                ('unit_price', models.DecimalField(decimal_places=1, max_digits=10)),
                ('count', models.PositiveIntegerField()),
                ('reason', models.CharField(max_length=512)),
                ('manufacturer', models.CharField(max_length=256)),
                ('apply_at', models.DateField()),
                ('accept_at', models.DateField(blank=True, null=True)),
                ('finish_at', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('model', models.CharField(max_length=256)),
                ('status', models.SmallIntegerField(choices=[(0, '正常'), (1, '维修中'), (2, '已报废')], default=0)),
                ('manager', models.CharField(max_length=256)),
                ('manufacturer', models.CharField(max_length=256)),
                ('purchase_at', models.DateTimeField()),
                ('scrap_at', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DeviceType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Repair',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.SmallIntegerField(choices=[(0, '修理中'), (1, '已完成')], default=0)),
                ('price', models.DecimalField(decimal_places=1, max_digits=12)),
                ('person_in_charge', models.CharField(max_length=256)),
                ('repair_manufacturer', models.CharField(max_length=256)),
                ('start_at', models.DateField()),
                ('finish_at', models.DateField(blank=True, null=True)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='lab.Device')),
            ],
        ),
        migrations.CreateModel(
            name='Scrap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scrap_at', models.DateField()),
                ('reason', models.CharField(max_length=512)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='lab.Device')),
            ],
        ),
        migrations.AddField(
            model_name='device',
            name='device_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='lab.DeviceType'),
        ),
        migrations.AddField(
            model_name='applyrecord',
            name='device_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='lab.DeviceType'),
        ),
    ]
