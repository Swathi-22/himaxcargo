from django.urls import path

from . import views

app_name='web'

urlpatterns = [
    path('', views.index,name='index'),
    path('about/', views.about,name='about'),
    path('services/', views.services,name='services'),
    path('gallery/',views.gallery,name='gallery'),
    path('updates/', views.updates,name='updates'),
    path('updates_details/<str:slug>/', views.updates_details,name='updates_details'),
    path('contact/', views.contact,name='contact'),
    path('order-tracking/',views.tracking,name='tracking'),
    path('order-tracking/<str:slug>/',views.live_tracking, name='live_tracking'),
    path('air_cargo/',views.air_cargo,name='air_cargo'),
    path('sea_cargo/',views.sea_cargo,name='sea_cargo'),
    path('port_to_port/',views.port_to_port,name='port_to_port'),
    path('moving_cargo/',views.moving_cargo,name='moving_cargo'),
    path('express_delivery/',views.express_delivery,name='express_delivery'),

]