from django.test import TestCase
from django.test import Client
from django.urls import reverse_lazy
from core.views import IndexView
from faker import Faker


class IndexViewTestCase(TestCase):

    def setUp(self):
        fake = Faker()
        self.dados = {
            'nome': fake.name(),
            'email': fake.email(),
            'assunto': fake.sentence(),
            'mensagem': fake.text(max_nb_chars=100),
        }
        self.dados_invalidos = {
            'nome': fake.name(),
            'assunto': fake.sentence(),
        }
        self.cliente = Client()
    

    def test_form_valid(self):
        request = self.cliente.post(reverse_lazy('index'), data=self.dados)
        self.assertEqual(request.status_code, 302)
    
    
    def test_form_invalid(self):
        request = self.cliente.post(reverse_lazy('index'), data=self.dados_invalidos)
        self.assertEqual(request.status_code, 200)
