from django.contrib import admin
from .models import Advertise, Hmtext, Autherroman, Competition, UserJvayez, Questions,abutkarbar, abutsaznde

# Register your models here.


admin.site.register(Advertise)
admin.site.register(Hmtext)
admin.site.register(Autherroman)


@admin.register(Competition)
class contact1(admin.ModelAdmin):
    list_display = ['user', 'id', 'roman']
    search_fields = ['user', 'roman']
    list_filter = ['bol']


@admin.register(Questions)
class contact12(admin.ModelAdmin):
    list_display = ['roman', 'id']
    search_fields = ['roman']


@admin.register(UserJvayez)
class contact2(admin.ModelAdmin):
    list_display = ['user', 'roman', 'id']
    search_fields = ['user', 'roman', 'id']

@admin.register(abutsaznde)
class contact4(admin.ModelAdmin):
    list_display = ['name', 'id', 'title']
    search_fields = ['name']


@admin.register(abutkarbar)
class contact5(admin.ModelAdmin):
    list_display = ['title', 'id']
    search_fields = ['title']
    
    
admin.site.site_header = 'پنل مدیریت سایت akoroman'
admin.site.index_title = 'پنل مدیریت'