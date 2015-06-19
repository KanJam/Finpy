from django.test import TestCase

# Create your tests here.

class FinpyViewsTestCase(TestCase):

	"""Classe que possui os métodos de teste 
	para as principais urls do sistema EqLibra.
	"""

	def test_login(self):

		"""Método que realiza um assert para verificar
		a conformidade entre requisição da página de login
		e obtenção da mesma.
		"""

		response_login = self.client.get('/finpy/login/')
		self.assertEqual(response_login.status_code, 200)

	def test_signup(self):

		"""Método que realiza um assert para verificar
		a conformidade entre requisição da página de cadastro 
		e obtenção da mesma.
		"""

		response_signup = self.client.get('/finpy/signup/')
		self.assertEqual(response_signup.status_code, 200)

	def test_entry_create(self):

		"""Método que realiza um assert para verificar
		a conformidade entre requisição da página de lançamento
		de receitas e despesas e a obtenção da mesma.
		"""

		response_entry_create = self.client.get('/finpy/entry/create/')
		self.assertEqual(response_entry_create.status_code, 302)

	def test_entry_list(self):

		"""Método que realiza um assert para verificar
		a conformidade entre requisição da página de listagem 
		de receitas e despesas lançadas e a obtenção da mesma.
		"""

		response_entry_list = self.client.get('/finpy/entry/list/')
		self.assertEqual(response_entry_list.status_code, 302)