from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from main.models import Tweet


class TweetListView(ListView):
    model = Tweet
    template_name = 'tweet_list.html' 
    context_object_name = 'tweet'


class TweetDetailView(DetailView):
    model = Tweet
    fields = '__all__'
    template_name = 'tweet_detail.html'
    context_object_name = 'tweet'
