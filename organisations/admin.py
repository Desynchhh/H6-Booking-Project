from django.contrib import admin

from .models import Organisation, OpeningHour

# Register your models here.

admin.site.register(Organisation)
admin.site.register(OpeningHour)