from django.contrib import admin
from .models import Registre
# Register your models here.

class Sign_upAdmin(admin.ModelAdmin):
    list_display = ("id","User_Name","Email","Contect_No","address")
    search_fields =('Email',)
    
admin.site.register(Registre,Sign_upAdmin)
