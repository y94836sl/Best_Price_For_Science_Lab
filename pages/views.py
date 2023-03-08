from django.shortcuts import render
from django.views.generic import TemplateView

from search import scrapy
import requests

from inventory.models import Product

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
	ExampleProducts = Product.objects.all()[:6]
	
	context = {
		'ExampleProducts': ExampleProducts,
	}
	if request.method == 'POST':
		return SearchResultView(request)
	else:
		
		return render(request, 'search.html', context)
	
def SearchResultView(request):
	if request.method == 'POST':
		query = request.POST.get('query')
		
		# Extract the data you want to scrape using BeautifulSoup's selectors
		results = scrapy.getResult(query)
		if request.method == 'POST':
			product_name = request.POST.get('product_name')
		
		# Render the data in a template
		return render(request, 'search.html', {'results': results})
	else:
		return render(request, 'home.html')
	
