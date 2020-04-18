from django.urls import path

from . import views

urlpatterns = [
    path('', views.comments, name='comments'),
    path('user_comments/', views.user_comments, name="user_comments"),
]