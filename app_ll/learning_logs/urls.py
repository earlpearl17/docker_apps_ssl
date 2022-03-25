"""Defines URL patterns for learning_logs."""

from django.conf.urls import url

from . import views

urlpatterns = [
	# Home page -> http://localhost:8000/
	url(r'^$', views.index, name='index'),
    
	# Show all topics -> http://localhost:8000/topics/
	url(r'^topics/$', views.topics, name='topics'),
    
  # Detail page for a single topic -> http://localhost:8000/topics/<id>/
	url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
	
	# Page for adding a new topic -> http://localhost:8000/new_topic/
	url(r'^new_topic/$', views.new_topic, name='new_topic'),
	
	# Page for adding a new entry -> http://localhost:8000/new_entry/<id>/
	url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
	
	# Page for editing an entry -> http://localhost:8000/edit_entry/<id>/
	url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry,name='edit_entry'),
]



