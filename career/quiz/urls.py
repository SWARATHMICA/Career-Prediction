from django.urls import path
from career import views

urlpatterns = [
    path('', views.predict, name='predict'),
    
]

