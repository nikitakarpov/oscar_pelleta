from django.db import models


class Price (models.Model):
    name=models.CharField(max_length=30, verbose_name='Тип упаковки')
    with_NO_NDS=models.IntegerField(verbose_name='Цена без НДС')
    with_NDS=models.IntegerField(verbose_name='Цена с НДС')

    class Meta:
        verbose_name = 'Цены'
        verbose_name_plural = 'Цены'

class Quality (models.Model):
    name=models.CharField(max_length=20, verbose_name='Название')
    value=models.CharField(max_length=20, verbose_name='Значение')

    class Meta:
        verbose_name = 'Качество'
        verbose_name_plural = 'Качество'


class FooterInfo (models.Model):
    name=models.CharField(max_length=20, verbose_name='Название')
    value = models.CharField(max_length=50, verbose_name='Значение')

    class Meta:
        verbose_name = 'Футер'
        verbose_name_plural = 'Футер'


class MessageFormModel (models.Model):
    datetime=models.DateTimeField(auto_now=True, verbose_name='Дата/Время')
    fio=models.CharField(max_length=50, verbose_name='Ф.И.О')
    phone=models.CharField(max_length=50, verbose_name='Телефон')
    email=models.CharField(max_length=50, verbose_name='Email', blank=True)
    text=models.TextField(verbose_name='Сообщение')

    class Meta:
        verbose_name = 'Заявки'
        verbose_name_plural = 'Заявки'

class OwnerEmailBox (models.Model):
    name = models.CharField(max_length=20, verbose_name='Название')
    value = models.CharField(max_length=50, verbose_name='Значение')

    class Meta:
        verbose_name = 'Ящик куда падают заявки'
        verbose_name_plural = 'Ящик куда падают заявки'

class TestImageModel (models.Model):
    name = models.CharField(max_length=20, verbose_name='Название')
    img = models.ImageField(upload_to='testimages/', verbose_name='Картинка' )

    class Meta:
        verbose_name = 'Тест Картинки'
        verbose_name_plural = 'Тест Картинки'

class ImagesModel (models.Model):
    name = models.CharField(max_length=20, verbose_name='Название')
    img = models.ImageField(upload_to='uploadimages/', verbose_name='Картинка' )

    class Meta:
        verbose_name = 'Картинки'
        verbose_name_plural = 'Картинки'