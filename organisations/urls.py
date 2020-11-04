from django.urls import path
from .views import (
    OrganisationDetailView,
)

app_name = 'organisations'

urlpatterns = [
    path('<int:pk>/<str:slug>/', OrganisationDetailView.as_view(), name='detail'),
]
