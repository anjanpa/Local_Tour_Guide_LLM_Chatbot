from django.urls import path
from .views.view_main import *

urlpatterns = [
    path('',home,name='home')
]
