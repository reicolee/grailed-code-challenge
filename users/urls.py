from django.urls import path
from users import views

urlpatterns = [
    path('', views.index),
    path('duplicate_users/', views.duplicate_users),
    path('disallowed_users/', views.disallowed_users),
]
