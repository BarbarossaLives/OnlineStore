from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.home, name='home'),
    path('api/products/', views.api_products, name='api_products'),
]
