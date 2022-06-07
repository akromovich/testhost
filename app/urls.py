from django.urls import path
from app import views

urlpatterns = [
    path('',views.index,name='index'),
    path('generic',views.generic,name='generic'),
    path('elements',views.elements,name='elements')
]