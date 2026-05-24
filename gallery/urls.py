from django.urls import path
from . import views

urlpatterns = [
    # Album URLs
    path('', views.album_list, name='album_list'),
    path('album/<int:pk>/', views.album_detail, name='album_detail'),
    path('album/create/', views.album_create, name='album_create'),
    path('album/<int:pk>/update/', views.album_update, name='album_update'),
    path('album/<int:pk>/delete/', views.album_delete, name='album_delete'),
    
    # Photo URLs
    path('album/<int:album_pk>/upload/', views.photo_upload, name='photo_upload'),
    path('photo/<int:pk>/', views.photo_detail, name='photo_detail'),
    path('photo/<int:pk>/delete/', views.photo_delete, name='photo_delete'),
]