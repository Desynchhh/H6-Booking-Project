from django.urls import path
from .views import (
    register,
    OrganisationDetailView,
    CreateOpeningFormView,
)

app_name = 'organisations'

urlpatterns = [
    path('register/', register, name='register'),
    path('<int:pk>/<str:slug>/', OrganisationDetailView.as_view(), name='detail'),
    path('<int:pk>/<str:slug>/opening-hours/', CreateOpeningFormView.as_view(), name='opening-hours'),
]
