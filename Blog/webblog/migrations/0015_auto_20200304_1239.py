# Generated by Django 3.0 on 2020-03-04 10:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webblog', '0014_auto_20200303_2039'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscibe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'ordering': ['date'],
            },
        ),
        migrations.AlterField(
            model_name='article',
            name='article_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 4, 12, 39, 20, 692761)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 4, 12, 39, 20, 694743)),
        ),
    ]
