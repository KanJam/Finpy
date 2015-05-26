from django.test import TestCase

# Create your tests here.

class FinpyViewsTestCase(TestCase):
	def test_login(self):
		response_login = self.client.get('/finpy/login/')
		self.assertEqual(response_login.status_code, 200)

	def test_signup(self):
		response_signup = self.client.get('/finpy/signup/')
		self.assertEqual(response_signup.status_code, 200)

	def test_entry_create(self):
		response_entry_create = self.client.get('/finpy/entry/create/')
		self.assertEqual(response_entry_create.status_code, 302)

	def test_entry_list(self):
		response_entry_list = self.client.get('/finpy/entry/list/')
		self.assertEqual(response_entry_list.status_code, 302)