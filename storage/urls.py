from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_storage, name='all_storage'),
]
