from django.db import models
from sorl_cropping import ImageRatioField

from sorl.thumbnail import get_thumbnail
from sorl_cropping.widgets import thumbnail

from sorl.thumbnail.fields import ImageField
from django.utils.html import format_html


# Create your models here.

class Slider(models.Model):
    img = ImageField(verbose_name='изображение слайдера', upload_to='slider_images')
    text = models.TextField(verbose_name='Текст', null=False, blank=True)
    active = models.BooleanField(default=True, verbose_name='Активно')

    img_crop = ImageRatioField('img', "800x300", verbose_name='Обрезка изображения')

    class Meta:
        verbose_name = "Слайдер"
        verbose_name_plural = "Слайдер"


class Gallery(models.Model):
    img = ImageField(verbose_name='изображение галереи', upload_to='gallery')
    img_crop = ImageRatioField('img', '1200x600', verbose_name='Обрезка фотографии')
    img_crop_thumbnail = ImageRatioField('img', '206x140', verbose_name='Обрезка миниатюры')

    text = models.TextField(verbose_name='Ифнормация', blank=True)
    title = models.CharField(max_length=255, verbose_name="Заголовок", blank=True)
    cdate = models.DateTimeField(verbose_name='Дата создания', auto_now=True)
    pdate = models.DateTimeField(verbose_name='Дата публикации', auto_now=True)
    prior = models.IntegerField(verbose_name='приоритет порядка отображения', default=0)

    active = models.BooleanField(verbose_name='Активное', default=True)

    def img_admin(self):
        return format_html(
            "<a href ='%s/change/'><img src='%s' ></a>" %
            (self.id, get_thumbnail(self.img, 'x80').url)
        )

    class Meta:
        verbose_name = "Фото"
        verbose_name_plural = "Фотографии"

# class Info(models.Model):
#     versionname = models.CharField(max_length=50, default='версия 1', unique=True)
#     section11 = models.TextField(blank=False, verbose_name='Блок Обо мне')
#
#     section21 = models.TextField(blank=False, verbose_name='блок 1 тренинги')
#     section22 = models.TextField(blank=False, verbose_name='блок 2 тренинги')
#     section23 = models.TextField(blank=False, verbose_name='блок 3 тренинги')
#
#     aforizm = models.TextField(blank=False, verbose_name='Блок Афоризма')
#
#     active = models.BooleanField(default=True)
#     created = models.DateTimeField (auto_now=True)
#
#     def __str__(self):
#         return self.versionname
