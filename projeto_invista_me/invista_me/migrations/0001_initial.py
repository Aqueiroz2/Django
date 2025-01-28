# Generated by Django 5.1.5 on 2025-01-28 03:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Investimento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('investimento', models.TextField(max_length=255)),
                ('valor', models.FloatField()),
                ('pago', models.BooleanField(default=False)),
                ('data', models.DateField(default=datetime.datetime.now)),
            ],
        ),
    ]
