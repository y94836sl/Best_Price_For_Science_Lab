from django.shortcuts import render
from django.views.generic import TemplateView

from search import scrapy
import requests

# Create your views here.
def HomePageView(request): 
	if request.method == 'POST':
		return SearchResultView(request)
	else:
		return render(request, 'home.html')
	
def AboutView(request):
	if request.method == 'POST':
		return SearchResultView(request)
	else:
		return render(request, 'about.html')
	
def SearchView(request):
	if request.method == 'POST':
		return SearchResultView(request)
	else:
		return render(request, 'search.html')
	
def SearchResultView(request):
	if request.method == 'POST':
		query = request.POST.get('query')
		
		# Extract the data you want to scrape using BeautifulSoup's selectors
		results = {}
		results['scrapy'] = scrapy.getResult(query)
		
		# Render the data in a template
		return render(request, 'search.html', {'results': results})
	else:
		return render(request, 'home.html')