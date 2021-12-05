from django.urls import path

from blog import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('<int:blog_id>/', views.blog_id, name="blogid"),
    path('categoria/<int:categoria_id>/', views.categoria, name="categoria"),
]