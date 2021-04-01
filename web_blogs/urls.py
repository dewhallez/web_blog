"""Defines URL patterns for web_blogs."""
from django.urls import path

from . import views

app_name = 'web_blogs'

urlpatterns = [
    # Home Page
    path('', views.index, name='index'),
    # Show topics.
    path('topics/', views.topics, name='topics'),
    # Detail page for a single topic
    path('topics/<int:topic_id>/', views.topic, name='topic'),
]
