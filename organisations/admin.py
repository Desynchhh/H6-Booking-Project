from django.contrib import admin

from .models import Organisation, OpeningHours

# Register your models here.

admin.site.register(Organisation)
admin.site.register(OpeningHours)