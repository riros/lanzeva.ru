from django.contrib import admin
from sorl_cropping import ImageCroppingMixin
from sorl.thumbnail.admin.current import AdminImageMixin
from www.models import Slider, Gallery
from django.db import models

from markitup.widgets import AdminMarkItUpWidget

from sorl_cropping.widgets import thumbnail

# Register your models here.

@admin.register(Slider)
class SliderAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ['id', 'img', 'text', 'active']
    list_filter = ['active']
    ordering = ['id']


@admin.register(Gallery)
class GalleryAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ['id', 'img_admin', 'text', 'active']
    # fieldsets = (
    #     (None, {
    #         'fields': ('img', 'img_crop_thumbnail', 'img_crop')
    #     }),
    # )
    list_filter = ['active']
    ordering = ['id']
    formfield_overrides = {
        models.TextField: {'widget': AdminMarkItUpWidget},
    }

# @admin.register(Info)
# class SliderAdmin(admin.ModelAdmin):
#     list_display = ['versionname', 'active', 'created']
