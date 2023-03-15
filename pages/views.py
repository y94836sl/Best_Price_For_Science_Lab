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
		
		try:
			# Extract the data you want to scrape using BeautifulSoup's selectors
			results = scrapy.getResult(query)
			
			if not results:
				# Show the "product not found" page
				return render(request, 'product_not_found.html')
			
			return render(request, 'search.html', {'results': results})
		except IndexError:
			# Show the "product not found" page
			return render(request, 'product_not_found.html')
		
			
	
#		if request.method == 'POST':
#			product_name = request.POST.get('product_name')
#		return render(request, 'search.html', {'results': results})
	else:
		return render(request, 'home.html')
	
	