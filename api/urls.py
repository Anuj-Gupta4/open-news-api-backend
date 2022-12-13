# from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('article-list', views.UserListView.as_view(), name="article-list"),
    path('article-create', views.articleCreate, name="article-create"),
    path('article-detail/<str:pk>/', views.articleDetail, name="article-detail"),
    path('article-update/<str:pk>/', views.articleUpdate, name="article-update"),
    path('article-delete/<str:pk>/', views.articleDelete, name="article-delete"),
]
