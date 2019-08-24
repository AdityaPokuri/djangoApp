from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name="Home"),
    path('about/', views.about, name="about"),
    path('gallery/', views.gallery, name="gallery"),
]