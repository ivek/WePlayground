from django.urls import path
from .views import HomePageView, SamplePageViews 

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('sample/', SamplePageViews.as_view(), name="sample"),
]