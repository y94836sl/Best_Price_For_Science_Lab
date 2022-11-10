#!/usr/bin/env python3
from bs4 import BeautifulSoup
import requests
import csv

result = {}

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

def scrapeTechbuyer(bs):
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

url =  "https://www.amazon.co.uk/s?k=Lenovo+ThinkCentre&crid=1NM9IGP0ZU0CL&sprefix=lenovo+thinkcentre%2Caps%2C176&ref=nb_sb_noss_1"

print(getAmazonProducts(getData(url)))