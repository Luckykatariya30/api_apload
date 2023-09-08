from django.contrib import admin
from .models import Registre

@admin.register(Registre)
class RegistreAdmin(admin.ModelAdmin):
    list_display = ['name','email','contact','address']

# Register your models here.
