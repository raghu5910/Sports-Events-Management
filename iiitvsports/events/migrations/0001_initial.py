# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-06-17 14:12
from __future__ import unicode_literals

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
            name='Cricket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('team_name', models.CharField(max_length=50)),
                ('Player1', models.CharField(max_length=50)),
                ('Player2', models.CharField(max_length=50)),
                ('Player3', models.CharField(max_length=50)),
                ('Player4', models.CharField(max_length=50)),
                ('Player5', models.CharField(max_length=50)),
                ('Player6', models.CharField(max_length=50)),
                ('Player7', models.CharField(max_length=50)),
                ('Player8', models.CharField(max_length=50)),
                ('Player9', models.CharField(max_length=50)),
                ('Player10', models.CharField(max_length=50)),
                ('Player11', models.CharField(max_length=50)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='crickets', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('event_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Football',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=50)),
                ('Player1', models.CharField(max_length=50)),
                ('Player2', models.CharField(max_length=50)),
                ('Player3', models.CharField(max_length=50)),
                ('Player4', models.CharField(max_length=50)),
                ('Player5', models.CharField(max_length=50)),
                ('Player6', models.CharField(max_length=50)),
                ('Player7', models.CharField(max_length=50)),
                ('Player8', models.CharField(max_length=50)),
                ('Player9', models.CharField(max_length=50)),
                ('Player10', models.CharField(max_length=50)),
                ('Player11', models.CharField(max_length=50)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='footballs', to='events.Event')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='footballs', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='cricket',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='crickets', to='events.Event'),
        ),
    ]
