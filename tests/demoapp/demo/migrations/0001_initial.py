# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-09 17:12
from __future__ import unicode_literals

import concurrency.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AutoIncConcurrentModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', concurrency.fields.AutoIncVersionField(db_column='cm_version_id', default=1, help_text='record revision number')),
                ('username', models.CharField(blank=True, max_length=30, null=True)),
                ('date_field', models.DateField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'AutoIncConcurrentModel',
                'verbose_name': 'AutoIncConcurrentModel',
            },
        ),
        migrations.CreateModel(
            name='ConcreteModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', concurrency.fields.IntegerVersionField(db_column='cm_version_id', default=1, help_text='record revision number')),
                ('username', models.CharField(blank=True, max_length=30, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ConditionalVersionModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', concurrency.fields.ConditionalVersionField(default=1, help_text='record revision number')),
                ('field1', models.CharField(blank=True, max_length=30, null=True, unique=True)),
                ('field2', models.CharField(blank=True, max_length=30, null=True, unique=True)),
                ('field3', models.CharField(blank=True, max_length=30, null=True, unique=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DropTriggerConcurrentModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', concurrency.fields.TriggerVersionField(db_column='cm_version_id', default=1, help_text='record revision number')),
                ('username', models.CharField(blank=True, max_length=30, null=True)),
                ('count', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='GroupTestModel',
            fields=[
                ('group_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.Group')),
                ('username', models.CharField(max_length=50, verbose_name='username')),
            ],
            bases=('auth.group',),
        ),
        migrations.CreateModel(
            name='Issue3TestModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=30, null=True)),
                ('last_name', models.CharField(blank=True, max_length=30, null=True)),
                ('char_field', models.CharField(blank=True, max_length=30, null=True)),
                ('date_field', models.DateField(blank=True, null=True)),
                ('version', models.CharField(blank=True, default='abc', max_length=10, null=True)),
                ('revision', concurrency.fields.IntegerVersionField(db_column='cm_version_id', default=1, help_text='record revision number')),
            ],
        ),
        migrations.CreateModel(
            name='ReversionConcurrentModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', concurrency.fields.IntegerVersionField(db_column='cm_version_id', default=1, help_text='record revision number')),
                ('username', models.CharField(blank=True, max_length=30, null=True, unique=True)),
                ('date_field', models.DateField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Reversion-ConcurrentModels',
                'verbose_name': 'Reversion-ConcurrentModel',
            },
        ),
        migrations.CreateModel(
            name='SimpleConcurrentModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', concurrency.fields.IntegerVersionField(db_column='cm_version_id', default=1, help_text='record revision number')),
                ('username', models.CharField(blank=True, max_length=30, null=True, unique=True)),
                ('date_field', models.DateField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'SimpleConcurrentModels',
                'verbose_name': 'SimpleConcurrentModel',
            },
        ),
        migrations.CreateModel(
            name='TriggerConcurrentModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', concurrency.fields.TriggerVersionField(db_column='cm_version_id', default=1, help_text='record revision number')),
                ('username', models.CharField(blank=True, max_length=30, null=True)),
                ('count', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': 'TriggerConcurrentModels',
                'verbose_name': 'TriggerConcurrentModel',
            },
        ),
        migrations.CreateModel(
            name='ConcurrencyDisabledModel',
            fields=[
                ('simpleconcurrentmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='demo.SimpleConcurrentModel')),
                ('dummy_char', models.CharField(blank=True, max_length=30, null=True)),
            ],
            bases=('demo.simpleconcurrentmodel',),
        ),
        migrations.CreateModel(
            name='CustomSaveModel',
            fields=[
                ('simpleconcurrentmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='demo.SimpleConcurrentModel')),
                ('extra_field', models.CharField(blank=True, max_length=30, null=True, unique=True)),
            ],
            bases=('demo.simpleconcurrentmodel',),
        ),
        migrations.CreateModel(
            name='InheritedModel',
            fields=[
                ('simpleconcurrentmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='demo.SimpleConcurrentModel')),
                ('extra_field', models.CharField(blank=True, max_length=30, null=True, unique=True)),
            ],
            bases=('demo.simpleconcurrentmodel',),
        ),
        migrations.CreateModel(
            name='ListEditableConcurrentModel',
            fields=[
            ],
            options={
                'verbose_name_plural': 'ListEditableConcurrentModels',
                'verbose_name': 'ListEditableConcurrentModel',
                'proxy': True,
            },
            bases=('demo.simpleconcurrentmodel',),
        ),
        migrations.CreateModel(
            name='NoActionsConcurrentModel',
            fields=[
            ],
            options={
                'verbose_name_plural': 'NoActions-ConcurrentModels',
                'verbose_name': 'NoActions-ConcurrentModel',
                'proxy': True,
            },
            bases=('demo.simpleconcurrentmodel',),
        ),
        migrations.CreateModel(
            name='ProxyModel',
            fields=[
            ],
            options={
                'verbose_name_plural': 'ProxyModels',
                'verbose_name': 'ProxyModel',
                'proxy': True,
            },
            bases=('demo.simpleconcurrentmodel',),
        ),
    ]
