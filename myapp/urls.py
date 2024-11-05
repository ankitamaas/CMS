# cms/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_content, name='view_content'),
    path('add/', views.add_content, name='add_content'),
    path('content/<int:content_id>/', views.content_detail, name='content_detail'),
    path('api/content/', views.view_content_api, name='view_content_api'),
]
