# Generated by Django 2.1 on 2018-11-17 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainPage', '0014_testimagemodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImagesModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Название')),
                ('img', models.ImageField(upload_to='uploadimages/', verbose_name='Картинка')),
            ],
            options={
                'verbose_name': 'Картинки',
                'verbose_name_plural': 'Картинки',
            },
        ),
    ]
