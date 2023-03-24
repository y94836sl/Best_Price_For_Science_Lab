#!/usr/bin/env python3
from bs4 import BeautifulSoup
import json
from urllib.parse import quote

import re
import requests

result = {}

def generateUrl(query):
    # Identify boolean search operators and process the query
    bool_operators = re.findall(r'\b(AND|OR)\b', query)
    words = re.split(r'\s+(?:AND|OR)\s+', query)
    
    if not bool_operators:
        bool_operators = ['OR'] * (len(words) - 1)
        
    # Combine the words and operators to form the final query
    processed_query = ' '.join(f'{quote(word)} {operator}' for word, operator in zip(words, bool_operators)) + quote(words[-1])
    
    # Generate Amazon URL from processed_query
    url1 = "https://www.amazon.co.uk/s?k=" + processed_query
    
    # Generate TechBuyer URL from processed_query
    url2 = "https://www.techbuyer.com/uk/catalogsearch/result/?q=" + processed_query
    
    # Generate Scientific Laboratory Supplies URL from processed_query
    url3 = "https://www.scientificlabs.co.uk/search/" + processed_query
    
    # Generate Farnell URL from processed_query
    url4 = "https://uk.farnell.com/search?st=" + processed_query + "&gs=true"
    
    return url1, url2, url3, url4

def getData(url):
    HEADERS = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
    }
    webpage = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(webpage.content, "lxml")
    return soup


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
    result["Scientific Laboratory Supplies "] = product
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

def getResult(query):
    """Scrape the information of products according to the user query"""
    url1, url2, url3, url4 = generateUrl(query)
    getAmazonProducts(getData(url1))
    getTechbuyerProducts(getData(url2))
    getScientificLabsProduct(getData(url3))
    getFarnellProduct(getData(url4))
    
    sortedDict = {}
    
    for supplier, value1 in result.items():
        for name, detail in value1.items():
            sortedDict2 = detail
            sortedDict2["supplier"] = supplier
            sortedDict[name] = dict(sortedDict2)
            
    sortedDict = dict(sorted(sortedDict.items(), key=lambda x: float(x[1]['price'].replace('£', '').replace('.', '').replace(',', '') ),))
    
    return sortedDict

#print(getResult("Ethanol"))
#print(getResult("Ammonium AND Persulfate OR Ethanol"))