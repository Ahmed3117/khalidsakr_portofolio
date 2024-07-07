from django import forms
from django.db import models
from django.contrib import admin
from .models import Notification

class NotificationAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_added', 'date_start', 'date_end', 'priority', 'status')
    search_fields = ('title', 'description')
    list_filter = ('priority', 'status')
    readonly_fields = ('date_added',)
    formfield_overrides = {
        models.TextField: {'widget': forms.Textarea(attrs={'rows': 4})},
    }

admin.site.register(Notification, NotificationAdmin)
