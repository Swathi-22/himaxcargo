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
]