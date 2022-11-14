#!/usr/bin/env python3
from bs4 import BeautifulSoup
import requests
import csv

result = {}

def generateUrl(query):
	# Generate Amazon URL from query
	query = query.replace(' ', '+')
	url1 = 'https://www.amazon.com/s?k=' + query
	# Generate TechBuyer URL from query
	# e.g. https://www.techbuyer.com/uk/catalogsearch/result/?q=lenovo+thinkcentre
	url2 = 'https://www.techbuyer.com/uk/catalogsearch/result/?q=' + query
	return url1, url2

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
	# Store scraped data in a dictionary
	n = len(nameList)
	products = {}
	for i in range(n):
		products[nameList[i]] = priceList[i]
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
	# Store scraped data in a dictionary
	n = len(nameList)
	products = {}
	for i in range(n):
		products[nameList[i]] = priceList[i]
	result['Techbuyer'] =  products
	return result

#url =  "https://www.amazon.co.uk/s?k=Lenovo+ThinkCentre&crid=1NM9IGP0ZU0CL&sprefix=lenovo+thinkcentre%2Caps%2C176&ref=nb_sb_noss_1"
query = 'Lenovo ThinkCentre'
url1, url2 = generateUrl(query)
getAmazonProducts(getData(url1))
getTechbuyerProducts(getData(url2))

print(result)
