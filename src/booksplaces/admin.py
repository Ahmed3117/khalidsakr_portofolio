from django.db import models
from django import forms
from django.contrib import admin
from .models import Library, Book, LibraryContact
from centersplaces.models import Government, Class

class BookInline(admin.TabularInline):
    model = Book
    extra = 1
    formfield_overrides = {
        models.TextField: {'widget': forms.Textarea(attrs={'rows': 2})},
    }

class LibraryContactInline(admin.TabularInline):
    model = LibraryContact
    extra = 1
class LibraryAdmin(admin.ModelAdmin):
    list_display = ('name', 'government', 'location', 'status')
    search_fields = ('name', 'location')
    list_filter = ('government', 'status')
    autocomplete_fields=('government',)
    inlines = [LibraryContactInline,BookInline]

class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'class_obj', 'library', 'status')
    search_fields = ('name', 'library__name')
    list_filter = ('class_obj', 'library', 'status')
    formfield_overrides = {
        models.TextField: {'widget': forms.Textarea(attrs={'rows': 2})},
    }

admin.site.register(Library, LibraryAdmin)
admin.site.register(Book, BookAdmin)
