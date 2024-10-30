from django.contrib import admin
from .models import Category, Essay

admin.site.register(Category)

class EssayAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'price')

admin.site.register(Essay, EssayAdmin)