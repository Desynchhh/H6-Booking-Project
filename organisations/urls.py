from django.urls import path
from .views import (
    register,
    OrganisationDetailView,
)

app_name = 'organisations'

urlpatterns = [
    path('register/', register, name='register'),
    path('<int:pk>/<str:slug>/', OrganisationDetailView.as_view(), name='detail'),
]
