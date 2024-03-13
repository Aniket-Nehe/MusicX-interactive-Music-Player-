from django.contrib import admin
from .models import song,ContactUs,Download
# Register your models here.
admin.site.register(song)

@admin.register(ContactUs)
class crudAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject','message']

@admin.register(Download)
class DownloadAdmin(admin.ModelAdmin):
    list_display= ['id','user','songs','download']