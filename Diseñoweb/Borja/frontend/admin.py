from django.contrib import admin
from .models import ExampleFrontendModel


@admin.register(ExampleFrontendModel)
class ExampleFrontendModelAdmin(admin.ModelAdmin):
    list_display = ('name',)
