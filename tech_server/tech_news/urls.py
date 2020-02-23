from django.urls import path, re_path
from . import views

urlpatterns = [
    path('new_feed/', views.News.as_view()),
    re_path('(?P<table_name>[^/]+)/', views.Manage_cate.as_view())
]
