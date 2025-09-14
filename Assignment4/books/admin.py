from django.contrib import admin
from .models import Genre, Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'genre', 'price')
    list_filter = ('genre', 'publication_year')
    search_fields = ('title', 'author')

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    search_fields = ('name',)