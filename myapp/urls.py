
from django.urls import path
from .views import priohub_data

urlpatterns = [
    path('priohub', priohub_data, name='priohub-data'),
]
