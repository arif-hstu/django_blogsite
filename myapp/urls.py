"""Defines URL patterns for myapp"""
from django.urls import path
from . import views
app_name = 'myapp'
urlpatterns = [
	# Home page
	path('', views.index, name='index'),
	# Topic page
	path('topics/', views.topics, name='topics'),
	# Individual topic page
	path('topics/<int:topic_id>/', views.topic, name='topic'),
	
]
