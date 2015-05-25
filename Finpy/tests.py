from django.test import TestCase

# Create your tests here.

class FinpyViewsTestCase(TestCase):
	def test_login(self):
		response_index = self.client.get('/finpy/login/')
		self.assertEqual(response_index.status_code, 200)

	def test_signup(self):
		response_update_profile = self.client.get('/finpy/signup/')
		self.assertEqual(response_update_profile.status_code, 200)