from django.contrib import admin
from django.urls import path
from Cake_Website import views

urlpatterns = [
    path('', views.index, name='home'),  # Root URL for home page
    path('about/', views.about, name='about'),  # Uncomment when the about view is ready
    path('services/', views.services, name='services'),  # Uncomment when the services view is ready
    path('contact/', views.contact, name='contact'),  # Uncomment when the contact view is ready
]
