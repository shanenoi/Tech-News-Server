from django.urls import path, re_path
from . import views

urlpatterns = [
    path('new_feed/', views.News.as_view()),
    path('categories/', views.categories),
    re_path('categories/(?P<table_name>[^/]+)/', views.Manage_cate.as_view())
]
