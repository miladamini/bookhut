from django.contrib import admin
from .models import FilmModel, zerfilm, Comments_film


# Register your models here.
@admin.register(FilmModel)
class contact1(admin.ModelAdmin):
    list_display = ['id', 'title']
    search_fields = ['title']


@admin.register(zerfilm)
class contact1(admin.ModelAdmin):
    list_display = ['id', 'title']
    search_fields = ['title']


@admin.register(Comments_film)
class contact1(admin.ModelAdmin):
    list_display = ['user', 'id', 'text']
