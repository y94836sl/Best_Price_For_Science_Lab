import unittest
from bs4 import BeautifulSoup
from scrapy import generateUrl, getData, getAmazonProducts,getAmazonProducts, getTechbuyerProducts, getScientificLabsProduct, getFarnellProduct, getResult

class TestWebScraper(unittest.TestCase):
	def test_generateUrl(self):
		query = "Ammonium AND Persulfate OR Ethanol"
		expected_urls = (
			"https://www.amazon.co.uk/s?k=Ammonium%20AND%20Persulfate%20OR%20Ethanol",
			"https://www.techbuyer.com/uk/catalogsearch/result/?q=Ammonium%20AND%20Persulfate%20OR%20Ethanol",
			"https://www.scientificlabs.co.uk/search/Ammonium%20AND%20Persulfate%20OR%20Ethanol",
			"https://uk.farnell.com/search?st=Ammonium%20AND%20Persulfate%20OR%20Ethanol&gs=true",
		)
	
		self.assertEqual(generateUrl(query), expected_urls)
	def test_generateUrl_no_operators(self):
			query = "Ethanol"
			expected_urls = (
				"https://www.amazon.co.uk/s?k=Ethanol",
				"https://www.techbuyer.com/uk/catalogsearch/result/?q=Ethanol",
				"https://www.scientificlabs.co.uk/search/Ethanol",
				"https://uk.farnell.com/search?st=Ethanol&gs=true",
			)
		
			self.assertEqual(generateUrl(query), expected_urls)
		
	def test_generateUrl_mixed_operators(self):
		query = "Ammonium AND Persulfate OR Nitrate AND Ethanol"
		expected_urls = (
			"https://www.amazon.co.uk/s?k=Ammonium%20AND%20Persulfate%20OR%20Nitrate%20AND%20Ethanol",
			"https://www.techbuyer.com/uk/catalogsearch/result/?q=Ammonium%20AND%20Persulfate%20OR%20Nitrate%20AND%20Ethanol",
			"https://www.scientificlabs.co.uk/search/Ammonium%20AND%20Persulfate%20OR%20Nitrate%20AND%20Ethanol",
			"https://uk.farnell.com/search?st=Ammonium%20AND%20Persulfate%20OR%20Nitrate%20AND%20Ethanol&gs=true",
		)
		
		self.assertEqual(generateUrl(query), expected_urls)
		
	def test_individual_scrapers(self):
		url1 = "https://www.amazon.co.uk/s?k=Ethanol"
		url2 = "https://www.techbuyer.com/uk/catalogsearch/result/?q=Ethanol"
		url3 = "https://www.scientificlabs.co.uk/search/Ethanol"
		url4 = "https://uk.farnell.com/search?st=Ethanol&gs=true"
		
		amazon_data = getAmazonProducts(getData(url1))
		techbuyer_data = getTechbuyerProducts(getData(url2))
		scientificlabs_data = getScientificLabsProduct(getData(url3))
		farnell_data = getFarnellProduct(getData(url4))
		
		self.assertTrue(amazon_data)
		self.assertTrue(techbuyer_data)
		self.assertTrue(scientificlabs_data)
		self.assertTrue(farnell_data)
		
	def test_getData(self):
		url = "https://www.amazon.co.uk/s?k=test"
		data = getData(url)
		self.assertIsInstance(data, BeautifulSoup)
		
	def test_getAmazonProducts(self):
		# This test assumes that the Amazon search result for "test" will always return some products.
		query = "test"
		url = f"https://www.amazon.co.uk/s?k={query}"
		soup = getData(url)
		result = getAmazonProducts(soup)
		self.assertIsInstance(result, dict)
		self.assertIn("Amazon", result)
		self.assertGreater(len(result["Amazon"]), 0)
		
	def test_getResult(self):
		query = "Ethanol"
		result = getResult(query)
	
		# Check if the result is not empty
		self.assertTrue(result)
	
		# Check if the result contains the expected keys (supplier names)
		self.assertIn("Amazon", result)
		self.assertIn("Techbuyer", result)
		self.assertIn("Scientific Laboratory Supplies", result)
		self.assertIn("Farnell", result)
	
		# Check if the result contains product names and details
		for supplier, products in result.items():
			self.assertTrue(products)
			for product_name, details in products.items():
				self.assertTrue(details["price"])
				self.assertTrue(details["url"])
		
	if __name__ == "__main__":
		unittest.main()
		