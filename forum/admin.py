from django.contrib import admin
from . import models


# Register your models here.
@admin.register(models.UserChatModel)
class a1(admin.ModelAdmin):
    list_display = ['user', 'id', 'p_time']
    search_fields = ['user', 'text']


@admin.register(models.Chatemodel)
class a2(admin.ModelAdmin):
    list_display = ['user', 'id', 'name']
    search_fields = ['user', 'name']
