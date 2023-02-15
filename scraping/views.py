from django.shortcuts import render
from django.views import generic

# For web Scraping
from bs4 import BeautifulSoup
import requests

# Create your views here.

result = {}
	
def getAmazonProducts(bs):
	"""Scrape the information of products in Amazon"""
	
	# Scrape product names
	names = bs.findAll("span", {"class": "a-size-medium a-color-base a-text-normal"})
	nameList = []
	for name in names:
		nameList.append(name.get_text())
	# Scrape product prices
	prices = bs.findAll("span", {"class": "a-offscreen"})
	priceList = []
	for price in prices:
		priceList.append(price.get_text())
	# Scrape product urls
	urls = bs.findAll(
		"a",
		{
			"class": "a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"
		},
	)
	urlList = []
	for url in urls:
		url = "https://www.amazon.co.uk/" + url.attrs["href"]
		urlList.append(url)
	# Store scraped data in a dictionary
	n = len(nameList)
	products = {}
	for i in range(n):
		details = {}
		details["price"] = priceList[i]
		details["url"] = urlList[i]
		products[nameList[i]] = details
	result["Amazon"] = products
	return result

def getTechbuyerProducts(bs):
	"""Scrape the information of products in TechBuyer"""
	# Scrape product names
	names = bs.findAll("a", {"class": "products__item-link"})
	nameList = []
	for name in names:
		nameList.append(name.get_text())
	# Delete the "\n"
	temp = []
	for n in nameList:
		temp.append(n.strip())
	nameList = temp
	
	# Scrape product prices
	prices = bs.findAll("span", {"class": "price"})
	priceList = []
	for price in prices:
		priceList.append(price.get_text())
		
	# Scrape product urls
	urls = bs.findAll("a", {"class": "products__item-link"})
	urlList = []
	for url in urls:
		urlList.append(url.attrs["href"])
	# Store scraped data in a dictionary
	n = len(nameList)
	products = {}
	# Store scraped data in a dictionary
	n = len(nameList)
	products = {}
	for i in range(n):
		details = {}
		details["price"] = priceList[i]
		details["url"] = urlList[i]
		products[nameList[i]] = details
	result["Techbuyer"] = products
	return result


def getScientificLabsProduct(bs):
	"""Scrape the information of products in Scientific Laboratory Supplies"""
	
	nameList = []
	urlList = []
	sizeList = []
	priceList = []
	
	# Scrape product details
	products = bs.findAll("div", {"class": "table-row"})
	for product in products:
		name_a = product.find(
			"a", href=True, title=True, style="color:black;", target=True
		)
		href = name_a.get("href")
		name = name_a.get("title")
		size_div = product.find(
			"div",
			{
				"class": "unit-size mobileGridCloserRows flex-100 indentedGridRow mobileDisplayContents range-unit"
			},
		)
		size = size_div.find("span", id=True).get_text()
		price = product.find("span", {"class": "gridDisplayBlock"}).get_text()
		
		nameList.append(name)
		urlList.append(href)
		sizeList.append(size)
		priceList.append(price)
		
	n = len(products)
	product = {}
	for i in range(n):
		details = {}
		details["size"] = sizeList[i]
		details["price"] = priceList[i]
		details["url"] = urlList[i]
		
		product[nameList[i]] = details
	result["ScientificLaboratorySupplies "] = product
	return result


def getFarnellProduct(bs):
	"""Scrape the information of products in Farnell"""
	nameL = []
	priceL = []
	urlL = []
	
	# Scrape product details
	descriptions = bs.findAll("td", {"class": "description enhanceDescClmn"})
	for d in descriptions:
		name = d.find("a", href=True).get("title")
		url = d.find("a", href=True).get("href")
		nameL.append(name)
		urlL.append(url)
	priceCol = bs.findAll("td", {"class": "listPrice enhanceQtyColumn"})
	for i in priceCol:
		price = i.find("span", {"class": "vatExcl"}).get_text()
		priceL.append(price)
	n = len(nameL)
	product = {}
	for i in range(n):
		details = {}
		details["price"] = priceL[i]
		details["url"] = urlL[i]
		
		product[nameL[i]] = details
	result["Farnell "] = product
	return result

#class ScrapeView(generic.CreateView):
def ScrapeView(request):
	if request.method == 'POST':
		query = request.POST.get('query')
		
		# Make a GET request to Amazon
		response = requests.get(f'https://www.amazon.co.uk/s?k={query}')
		# Parse the HTML content of the response using BeautifulSoup
		bs = BeautifulSoup(response.content, "lxml")
		getAmazonProducts(bs)
		
		# Make a GET request to TechBuyer
		response2 = requests.get(f'https://www.techbuyer.com/uk/catalogsearch/result/?q={query}')		# Parse the HTML content of the response using BeautifulSoup
		bs2 = BeautifulSoup(response2.content, "lxml")
		getTechbuyerProducts(bs2)
		
		# Make a GET request to Scientific Laboratory Supplies 
		response3 = requests.get(f'https://www.scientificlabs.co.uk/search/{query}')
		# Parse the HTML content of the response using BeautifulSoup
		bs3 = BeautifulSoup(response3.content, "lxml")
		getTechbuyerProducts(bs3)
		
		# Make a GET request to Scientific Laboratory Supplies 
		response4 = requests.get(f'https://uk.farnell.com/search?st={query}&gs=true')
		# Parse the HTML content of the response using BeautifulSoup
		bs4 = BeautifulSoup(response4.content, "lxml")
		getTechbuyerProducts(bs4)
		
		# Render the data in a template
		return render(request, 'search.html', {'results': results})
	
		if not (response.status_code==200 and response2.status_code==200 and response3.status_code==200):
			# Return an error if the request was not successful
			return render(request, 'error.html')
	else:
		return render(request, 'home.html')
	