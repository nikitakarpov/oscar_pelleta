# Generated by Django 2.1 on 2018-09-12 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainPage', '0008_auto_20180913_0050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messegeform',
            name='email',
            field=models.CharField(blank=True, max_length=50, verbose_name='Email'),
        ),
    ]
