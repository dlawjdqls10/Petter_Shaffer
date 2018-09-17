from django.contrib import admin
from .models import Show, Circle, Cast

# Register your models here.


@admin.register(Show)
class ShowAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(Circle)
class CircleAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Cast)
class CastAdmin(admin.ModelAdmin):
    list_display = ['name']
