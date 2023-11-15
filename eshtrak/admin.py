from django.contrib import admin
from .models import tkfifcode, Day1, ssion ,buy

# Register your models here.


admin.site.register(tkfifcode)

@admin.register(buy)
class contact2(admin.ModelAdmin):
    list_display = ['user','roman', 'id']
    search_fields = ['user','roman', 'id']


@admin.register(Day1)
class contact2(admin.ModelAdmin):
    list_display = ['user', 'id']
    search_fields = ['id']


@admin.register(ssion)
class ssionadmin(admin.ModelAdmin):
    list_display = ['user', 'id']
    search_fields = ['id']
