from django.contrib import admin
from core.models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('created_on', 'name', 'email')

admin.site.register(Contact, ContactAdmin)
