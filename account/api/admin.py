from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from .models import User

class UserModelAdmin(UserAdmin):

    list_display = ['id', 'email', 'name', 'is_admin']
    list_filter = ['is_admin']
    fieldsets = [
        
        ('User credentials',{'fields':['email','password']}),
        ('personal info', {'fields':['name']}),
        ('permissions',{'fields': ['is_admin']}),
    ]
    add_fieldsets = [
        (
            None ,
            {
                'classes': ['wide'],
                'fields': ['email','name','password1','password2']
            },
        ),
    ]

    search_fields = ['email']
    ordering = ['email','id']
    filter_horizontal =[]

admin.site.register(User,UserModelAdmin)

