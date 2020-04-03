from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView 
from django.urls import reverse_lazy


from .models import Page

# Create your views here.
class PageListView(ListView):
    model= Page

class PageDetailView(DetailView):
    model= Page

class PageCreateView(CreateView):
    model= Page
    fields= ['title', 'content']
    success_url= reverse_lazy('pages:pages')