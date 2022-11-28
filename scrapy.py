#!/usr/bin/env python3
from bs4 import BeautifulSoup
import requests
import csv

result = {}

def generateUrl(query):
	# Generate Amazon URL from query
	query = query.replace(' ', '+')
	url1 = 'https://www.amazon.co.uk/s?k=' + query
	# Generate TechBuyer URL from query
	# e.g. https://www.techbuyer.com/uk/catalogsearch/result/?q=lenovo+thinkcentre
	url2 = 'https://www.techbuyer.com/uk/catalogsearch/result/?q=' + query
	# Generate scientific laboratory supplies URL from query
	# e.g. https://www.scientificlabs.co.uk/search/ethanol
	url3 = 'https://www.scientificlabs.co.uk/search/' + query
	return url1, url2, url3

def getData(url):
	HEADERS = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'}
	webpage = requests.get(url, headers=HEADERS)
	soup = BeautifulSoup(webpage.content, "lxml")
	return soup

def getAmazonProducts(bs):
	
	# Scrape product names
	names = bs.findAll('span',{'class':'a-size-medium a-color-base a-text-normal'})
	nameList = []
	for name in names:
		nameList.append(name.get_text())
	# Scrape product prices
	prices = bs.findAll('span',{'class':'a-offscreen'})
	priceList = []
	for price in prices:
		priceList.append(price.get_text())
	# Scrape product urls
	urls = bs.findAll('a',{'class':'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'})
	urlList = []
	for url in urls:
		url = 'https://www.amazon.co.uk/' + url.attrs['href']
		urlList.append(url)
	# Store scraped data in a dictionary
	n = len(nameList)
	products = {}
	for i in range(n):
		details = {}
		details['price'] = priceList[i]
		details['url'] = urlList[i]
		products[nameList[i]] = details
	result['Amazon'] =  products
	return result

def getTechbuyerProducts(bs):
	# Scrape product names
	names = bs.findAll('a',{'class':'products__item-link'})
	nameList = []
	for name in names:
		nameList.append(name.get_text())
	# Delete the "\n"
	temp = []
	for n in nameList:
		temp.append(n.strip())
	nameList = temp
	
	# Scrape product prices
	prices = bs.findAll('span',{'class':'price'})
	priceList = []
	for price in prices:
		priceList.append(price.get_text())
	
	# Scrape product urls
	urls = bs.findAll('a',{'class':'products__item-link'})
	urlList = []
	for url in urls:
		urlList.append(url.attrs['href'])
	# Store scraped data in a dictionary
	n = len(nameList)
	products = {}
	# Store scraped data in a dictionary
	n = len(nameList)
	products = {}
	for i in range(n):
		details = {}
		details['price'] = priceList[i]
		details['url'] = urlList[i]
		products[nameList[i]] = details
	result['Techbuyer'] =  products
	return result

def getScientificLabsProduct(bs):
	nameList = []
	urlList = []
	sizeList = []
	priceList = []
	
	# Scrape product details
	products = bs.findAll('div', {'class':'table-row'})
	for product in products:
		name_a = product.find('a',href=True, title=True, style="color:black;", target=True)
		href = name_a.get('href')
		name = name_a.get('title')
		size_div = product.find('div',{'class':'unit-size mobileGridCloserRows flex-100 indentedGridRow mobileDisplayContents range-unit'})
		size = size_div.find('span', id=True).get_text()
		price = product.find('span',{'class':'gridDisplayBlock'}).get_text()
		
		nameList.append(name)
		urlList.append(href)
		sizeList.append(size)
		priceList.append(price)
		
	n = len(products)
	product = {}
	for i in range(n):
		details = {}
		details['size'] = sizeList[i]
		details['price'] = priceList[i]
		details['url'] = urlList[i]
		
		product[nameList[i]] = details
	result['ScientificLaboratorySupplies '] =  product
	return result

query = 'Ethanol'
url1, url2, url3 = generateUrl(query)
getAmazonProducts(getData(url1))
getTechbuyerProducts(getData(url2))
getScientificLabsProduct(getData(url3))

print(result)
