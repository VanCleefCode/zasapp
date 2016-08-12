from django.contrib import admin
from .models import Contacto
# Register your models here.
class ContactoAdmin(admin.ModelAdmin):
    pass
admin.site.register(Contacto, ContactoAdmin)
