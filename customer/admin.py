from django.contrib import admin
from .models import Customer

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_num','address','client')

admin.site.register(Customer, CustomerAdmin)
