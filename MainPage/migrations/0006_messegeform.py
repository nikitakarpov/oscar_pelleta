# Generated by Django 2.1 on 2018-09-12 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainPage', '0005_auto_20180912_1941'),
    ]

    operations = [
        migrations.CreateModel(
            name='MessegeForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.CharField(max_length=50, verbose_name='Ф.И.О')),
                ('phone', models.CharField(max_length=50, verbose_name='Телефон')),
                ('email', models.CharField(max_length=50, verbose_name='Email')),
                ('text', models.TextField(verbose_name='Сообщение')),
            ],
        ),
    ]