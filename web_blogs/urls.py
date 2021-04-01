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
    # Page for adding new topics
    path('new_topic/', views.new_topic, name='new_topic'),
    # Page for adding new entry
    path('new_entry/<int:topic_id>', views.new_entry, name='new_entry'),
    # PAge for editing entry
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]
