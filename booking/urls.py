from django.urls import path
from .views import *

app_name = 'booking'

urlpatterns = [
    path('', temp_home, name='temp-home'),
]