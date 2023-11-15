from django.contrib import admin

from . import models


@admin.action(description="Mark selected stories as published")
def make_published(modeladmin, request, queryset):
    queryset.update(status="p")


# Register your models here.
class zir(admin.TabularInline):
    model = models.Part_roman


@admin.register(models.post)
class PostAdmin(admin.ModelAdmin):
    actions = ("uppercase", "lowercase")  # Necessary

    @admin.action(description='حذف کردن از لیست ربات')
    def uppercase(modeladmin, request, queryset):
        for obj in queryset:
            obj.botmodel = False
            obj.save()

    list_display = ['title', 'view', 'Accepted', 'eshtrak', 'correction', 'id']
    list_filter = ['Accepted', 'eshtrak', 'correction']
    # inlines = (zir,)
    search_fields = ['title', 'slug', 'correction']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(models.Podcast)
class podcastAdmin(admin.ModelAdmin):
    list_display = ['title', 'view', 'correction', 'eshtrak']
    list_filter = ['Accepted', 'eshtrak']
    search_fields = ['title', 'slug']


@admin.register(models.Tamas_ba_ma)
class contact1(admin.ModelAdmin):
    list_display = ['user', 'id', 'name']
    search_fields = ['user', 'name']


@admin.register(models.Comments_post)
class contact1(admin.ModelAdmin):
    list_display = ['user', 'id', 'text']


@admin.register(models.Comments_Podcast)
class contact1(admin.ModelAdmin):
    list_display = ['user', 'id', 'text']


@admin.register(models.Part_roman)
class contact2(admin.ModelAdmin):
    actions = ("uppercase", "lowercase")  # Necessary

    @admin.action(description='تبدیل به pdf')
    def uppercase(modeladmin, request, queryset):
        for obj in queryset:
            obj.Pdf = True
            obj.save()

    @admin.action(description='حذف از pdf')
    def lowercase(modeladmin, request, queryset):
        for obj in queryset:
            obj.Pdf = False
            obj.save()

    list_display = ['roman', 'id', 'name']
    search_fields = ['roman', 'name']
    list_filter = ['roman']
    autocomplete_fields = ['roman']


@admin.register(models.Part_pad)
class contact3(admin.ModelAdmin):
    list_display = ['body', 'id', 'name']
    search_fields = ['pad', 'body']
