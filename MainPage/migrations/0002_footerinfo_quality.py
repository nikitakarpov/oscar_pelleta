# Generated by Django 2.1 on 2018-09-12 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainPage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FooterInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, verbose_name='Название')),
                ('value', models.CharField(max_length=15, verbose_name='Значение')),
            ],
        ),
        migrations.CreateModel(
            name='Quality',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, verbose_name='Название')),
                ('value', models.CharField(max_length=10, verbose_name='Значение')),
            ],
        ),
    ]
