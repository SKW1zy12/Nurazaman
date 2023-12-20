from django.contrib import admin
from apps.contacts import models
# Register your models here.

class ContactsFilterAdmin(admin.ModelAdmin):
    list_filter = ('name', )
    list_display = ('name', 'email')
    search_fields = ('name', 'email')

admin.site.register(models.Contacts, ContactsFilterAdmin)
