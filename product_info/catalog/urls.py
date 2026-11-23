from django.urls import path
from . import views

urlpatterns = [
    # Displays main page at category/
    path('', views.main_page, name='main_page')
]