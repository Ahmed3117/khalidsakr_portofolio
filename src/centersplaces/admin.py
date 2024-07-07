from django.contrib import admin
from .models import CenterContact, Government, Center, Class, Dates

class CenterInline(admin.TabularInline):
    model = Center
    extra = 1
class CenterContactInline(admin.TabularInline):
    model = CenterContact
    extra = 1

class DatesInline(admin.TabularInline):
    model = Dates
    extra = 1
    autocomplete_fields=('class_obj',)

class GovernmentAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    # inlines = [CenterInline]

class CenterAdmin(admin.ModelAdmin):
    list_display = ('name','government', 'location', 'status')
    search_fields = ('location',)
    list_filter = ('government', 'status')
    autocomplete_fields=('government',)
    inlines = [CenterContactInline,DatesInline]

class ClassAdmin(admin.ModelAdmin):
    list_display = ('name', 'status')
    search_fields = ('name',)
    list_filter = ('status',)

class DatesAdmin(admin.ModelAdmin):
    list_display = ('center', 'class_obj', 'date_day','date_time', 'status')
    search_fields = ('center__location', 'class_obj__name')
    list_filter = ('status', 'center', 'class_obj','date_day')

admin.site.register(Government, GovernmentAdmin)
admin.site.register(Center, CenterAdmin)
admin.site.register(Class, ClassAdmin)
admin.site.register(Dates, DatesAdmin)
