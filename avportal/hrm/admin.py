from django.contrib import admin
from .models import Detail
from django.utils.html import format_html
# Register your models here.
class DetailAdmin(admin.ModelAdmin):
    def thumbnail(self,object):
        return format_html('<img src="{}" width="40" style="border-radius:50px"/>'.format(object.photos.url))

    thumbnail.short_description = 'photo'

    list_display = ('emp_id','thumbnail','first_name','last_name','email','project')
    list_display_links = ('emp_id','thumbnail','first_name')
    search_fields = ('first_name','last_name')
    # list_filter = ('designation',)
admin.site.register(Detail, DetailAdmin)