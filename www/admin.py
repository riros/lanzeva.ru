from django.contrib import admin
from sorl_cropping import ImageCroppingMixin
from sorl.thumbnail.admin.current import AdminImageMixin
from www.models import Slider, Gallery, Blog
from django.db import models


from markitup.widgets import AdminMarkItUpWidget

# Register your models here.

@admin.register(Slider)
class SliderAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ['id', 'img', 'text', 'active']
    list_filter = ['active']
    ordering = ['id']


@admin.register(Gallery)
class GalleryAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ['id', 'pdate', 'img_admin', 'text', 'active']
    # fieldsets = (
    #     (None, {
    #         'fields': ('img', 'img_crop_thumbnail', 'img_crop')
    #     }),
    # )
    list_filter = ['active']
    ordering = ['id']
    formfield_overrides = {
        models.TextField: {'widget': AdminMarkItUpWidget(attrs={'style': 'height: 65px;'})},
    }
    list_editable = [
        'pdate', 'text', 'active'
    ]


@admin.register(Blog)
class BlogAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ['id',
                    Blog.pdate.field_name,
                    'img_admin',
                    Blog.text.field_name,
                    Blog.active.field_name
                    ]
    list_editable = [
        'pdate', 'text', 'active'
    ]
    list_filter = ['active']
    ordering = ['-pdate', 'cdate']
    formfield_overrides = {
        models.TextField: {'widget': AdminMarkItUpWidget(attrs={'style': 'height: 65px;'})},
    }

# @admin.register(Info)
# class SliderAdmin(admin.ModelAdmin):
#     list_display = ['versionname', 'active', 'created']



admin.site.site_header = 'Администрирование lanzeva.ru'
admin.site.site_title = 'Администрирование'
admin.site.index_title = 'Начало'