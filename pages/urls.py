from django.urls import path
from .views import HomePageView, AboutView, SearchView, SearchResultView

urlpatterns = [
    path('', HomePageView, name='home'),
    path('about/', AboutView, name='about'),
    path('search/', SearchView, name='search'),
    path("searchResult/", SearchResultView, name="searchResult"),
]
