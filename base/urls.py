from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('property/',views.Property,name='property'),
    path('register-property/',views.Registerproperty,name='regprop'),
    path('search/',views.PropertySearch,name='search'),
    path('contact-us/',views.contact,name='contact'),
    path('view-property/',views.View,name='view'),
    path('update-property/<str:pk>/', views.update_property, name="update-property"),
    path('delete-property/<str:pk>/', views.delete_property, name="delete-property"),
]
