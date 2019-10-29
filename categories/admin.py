from django.contrib import admin
from .models import Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'get_icon', 'short_detail', 'date_created', 'last_updated']
    search_fields = ['name', 'detail']
    fieldsets = [
        ('NAME', {
            'fields': ['name'],
        }),
        ('ICON', {
            'fields': ['icon'],
        }),
        ('DETAIL', {
            'fields': ['detail'],
        }),
    ]

admin.site.register(Category, CategoryAdmin)