import unittest
from bs4 import BeautifulSoup
from scrapy import generateUrl, getData, getAmazonProducts, getResult

class TestWebScraper(unittest.TestCase):
	def test_generateUrl(self):
		query = "Ethanol"
		expected_amazon_url = "https://www.amazon.co.uk/s?k=Ethanol"
		expected_techbuyer_url = "https://www.techbuyer.com/uk/catalogsearch/result/?q=Ethanol"
		expected_scientific_labs_url = "https://www.scientificlabs.co.uk/search/Ethanol"
		expected_farnell_url = "https://uk.farnell.com/search?st=Ethanol&gs=true"
		
		urls = generateUrl(query)
		
		self.assertEqual(urls[0], expected_amazon_url)
		self.assertEqual(urls[1], expected_techbuyer_url)
		self.assertEqual(urls[2], expected_scientific_labs_url)
		self.assertEqual(urls[3], expected_farnell_url)
		
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
		self.assertIsInstance(result, dict)
		self.assertGreater(len(result), 0)
		
	if __name__ == "__main__":
		unittest.main()
		