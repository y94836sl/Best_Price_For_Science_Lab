from django.shortcuts import render
from django.views.generic import TemplateView

from search import scrapy
import requests

from inventory.models import Product
import re


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

# ------------------------------ #
# ------- Boolean Search ------- #
# ------------------------------ #

def process_boolean_query(query):
	# Replace boolean operators with their corresponding symbols
	query = re.sub(r'\bAND\b', '&', query, flags=re.IGNORECASE)
	query = re.sub(r'\bOR\b', '|', query, flags=re.IGNORECASE)
	query = re.sub(r'\bNOT\b', '!', query, flags=re.IGNORECASE)
	
	# You can add more preprocessing steps here if needed
	
	return query

# ------------------------------ #
# -----------  Search ---------- #
# ------------------------------ #
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
		
		query.lower()
		# Preprocess the query to handle boolean search
		processed_query = process_boolean_query(query)
		
		try:
			# Extract the data you want to scrape using BeautifulSoup's selectors
			results = scrapy.getResult(query)
#			results = scrapy.getResult(query)
			
			
			if not results:
				# Show the "product not found" page
				return render(request, 'product_not_found.html')
			
			return render(request, 'search.html', {'results': results})
		except IndexError:
			# Show the "product not found" page
			return render(request, 'product_not_found.html')
	else:
		return render(request, 'home.html')
	
	