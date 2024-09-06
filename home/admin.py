from django.contrib import admin
from .models import ListModel

@admin.register(ListModel)
class ListAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'date', 'time')