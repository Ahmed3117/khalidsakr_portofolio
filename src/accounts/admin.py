from django import forms
from django.contrib import admin
from .models import Account, Phone, SocialAccount
from django.db import models
# from django.utils.html import mark_safe 


class PhoneInline(admin.TabularInline):
    model = Phone
    extra = 1
    

class SocialAccountInline(admin.TabularInline):
    model = SocialAccount
    extra = 1
    

class AccountAdmin(admin.ModelAdmin):
    list_display = ('name', 'mail', 'address')
    search_fields = ('name', 'mail', 'address')
    inlines = [PhoneInline, SocialAccountInline]
    max_num = 1
    formfield_overrides = {
        models.TextField: {'widget': forms.Textarea(attrs={'rows': 3})},
    }
    def has_add_permission(self, request):
        # Check if any Account objects exist
        return not Account.objects.exists()

    # def logo_display(self, obj):
    #     if obj.logo:
    #         return mark_safe(f'<img src="{obj.logo}" width="200" height="50" alt="Logo" />')
    #     else:
    #         return 'No Logo'

    # logo_display.allow_tags = True
    # logo_display.short_description = 'Logo'


class PhoneAdmin(admin.ModelAdmin):
    list_display = ('account', 'phone_number')
    search_fields = ('phone_number',)
    list_filter = ('account',)

class SocialAccountAdmin(admin.ModelAdmin):
    list_display = ('account', 'site', 'url', 'is_active', 'icon_display')
    list_filter = ('is_active', 'account')
    search_fields = ('site', 'url')
    readonly_fields = ('icon_display',)
    
    def icon_display(self, obj):
        if obj.icon:
            return f'<img src="{obj.icon.url}" width="30" height="30"/>'
        return 'No Icon'
    icon_display.allow_tags = True
    icon_display.short_description = 'Icon'

admin.site.register(Account, AccountAdmin)
admin.site.register(Phone, PhoneAdmin)
admin.site.register(SocialAccount, SocialAccountAdmin)
