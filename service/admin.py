from django.contrib import admin
from .models import Service

class ServiceAdmin(admin.ModelAdmin):
    list_display =('service_icon','service_title','servic_des')


admin.site.register(Service,ServiceAdmin)

# Register your models here.
