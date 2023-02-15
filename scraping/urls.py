from django.urls import path
from . import ScrapeView

urlpatterns = [
    path('scrape/', ScrapeView.as_view(), name='scrape'),
]