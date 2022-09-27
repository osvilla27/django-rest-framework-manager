# Generated by Django 4.1.1 on 2022-09-27 15:57

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_remove_spent_month_remove_spent_year_spent_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 9, 27, 10, 57, 24, 837595)),
        ),
        migrations.AlterField(
            model_name='spent',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 9, 27, 10, 57, 24, 837595)),
        ),
        migrations.CreateModel(
            name='DaySpent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.datetime(2022, 9, 27, 10, 57, 24, 837595))),
                ('total', models.FloatField(default=0)),
                ('description', models.CharField(blank=True, max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.store')),
            ],
        ),
    ]
