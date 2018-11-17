from django.contrib import admin
from .models import Price, Quality, FooterInfo, MessageFormModel, OwnerEmailBox, ImagesModel, TestImageModel


class PriceAdmin(admin.ModelAdmin):
    list_display = ('name', 'with_NO_NDS', 'with_NDS') # поля отображаються в админке
    fields = ('with_NO_NDS', 'with_NDS') #для редактирования доступнытолько цены

class QualityAdmin(admin.ModelAdmin):
    list_display = ('name', 'value')
    fields = ('value',)

class FooterInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'value')
    fields = ('value',)


class MessageFormModelAdmin(admin.ModelAdmin):
    list_display = ('fio', 'phone', 'email', 'text','datetime')
    search_fields = ('fio', 'phone', 'email', 'text','datetime')
    readonly_fields = ('fio', 'phone', 'email', 'text','datetime') # данные поля олько для чтения

class OwnerEmailBoxAdmin(admin.ModelAdmin):
    list_display = ('name', 'value')
    fields = ('value',)

class TestImageModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'img') # поля отображаються в админке
    fields = ('name', 'img') #для редактирования доступнытолько цены

class ImagesModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'img')
    fields = ('img',)

admin.site.register(Price, PriceAdmin)
admin.site.register(Quality, QualityAdmin)
admin.site.register(FooterInfo, FooterInfoAdmin)
admin.site.register(MessageFormModel, MessageFormModelAdmin)
admin.site.register(OwnerEmailBox, OwnerEmailBoxAdmin)
admin.site.register(ImagesModel, ImagesModelAdmin)
#admin.site.register(TestImageModel, TestImageModelAdmin)

