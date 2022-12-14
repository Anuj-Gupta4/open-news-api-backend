# from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('article-list', views.UserListView.as_view(), name="article-list"),
    path('article-search', views.UserSearchView.as_view(), name="article-search"),
    path('article-list/national', views.NationalView.as_view(), name="national"),
    path('article-list/fashion', views.FashionView.as_view(), name='fashion'),
    path('article-list/sports', views.SportsView.as_view(), name='sports'),
    path('article-list/politics', views.PoliticsView.as_view(), name='politics'),
    path('article-list/others', views.OthersView.as_view(), name='others'),
    path('article-list/finance', views.FinanceView.as_view(), name='finance'),
    path('article-create', views.articleCreate, name="article-create"),
    path('article-detail/<str:pk>/', views.articleDetail, name="article-detail"),
    path('article-update/<str:pk>/', views.articleUpdate, name="article-update"),
    path('article-delete/<str:pk>/', views.articleDelete, name="article-delete"),
]
