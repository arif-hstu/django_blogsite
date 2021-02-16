from django.shortcuts import render

# My import
from .models import Topic

# Create your views here.

# Index template view
def index(request):
	"""The home page for My_app."""
	return render(request, 'myapp/index.html')

# Topics view
def topics(request):
	"""Show all topics."""
	topics = Topic.objects.order_by('date_added')
	context = {'topics': topics}
	return render(request, 'myapp/topics.html', context)

# topic view
def topic(request, topic_id):
	'''show a single topic and all its entries.'''
	topic = Topic.objects.get(id=topic_id)
	entries = topic.entry_set.order_by('-date_added')
	context = {'topic':topic, 'entries': entries}
	return render(request, 'myapp/topic.html', context)
