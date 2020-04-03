from django.urls import path
from . import views
from .views import PageListView, PageDetailView, PageCreateView

pages_patterns = ([
    path('', PageListView.as_view(),  name='pages'),
    path('new/', PageCreateView.as_view(),  name='create'),
    path('<int:pk>/<slug:page_slug>/', PageDetailView.as_view(), name='page'),
], 'pages')