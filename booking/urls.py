from django.urls import path
from .views import *

app_name = 'booking'

urlpatterns = [
    path('', OrganisationListView.as_view(), name='organisation-list'),
    path('booking/<int:pk>/<str:slug>/', OrganisationDetailView.as_view(), name='organisation-detail'),
]
