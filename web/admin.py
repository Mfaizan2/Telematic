from django.contrib import admin
from .models import Web

class WebAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_num','address', 'customer')

admin.site.register(Web, WebAdmin)