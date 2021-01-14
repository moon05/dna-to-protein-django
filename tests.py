from django.test import TestCase
from django.test import Client
# from unittest import IsolatedAsyncioTestCase



client = Client()

class SimpleTestSuite(TestCase):

	def test_index(self):
		response = self.client.get('/dnatoprotein/')
		self.assertEqual(response.status_code, 200)

	def test_dna_search_url(self):
		response = self.client.get('/dnatoprotein/search')
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "No Input")

	def test_dna_search_with_no_query(self):
		response = self.client.get('/dnatoprotein/search?q')
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "Empty String/Invalid Input")


# even though the documentation for unittest says this works
# I couldn't get this to work on my machine
# I kept getting this error: NameError: name 'AsyncConnection' is not defined
# so for now the query testing isn't enabled

# class AsyncTest(IsolatedAsyncioTestCase):
# 	async def asyncSetUp(self):
# 		self.connection = await AsyncConnection()

# 	async def test_dna_search_no_success(self):
# 		response = await self.connection.get('/dnatoprotein/search?q=ABCDE')
# 		self.assertEqual(response.status_code, 200)
# 		self.assertContains(response, {"success":0})

# 	async def asyncTearDown(self):
# 		await self.connection.close()
