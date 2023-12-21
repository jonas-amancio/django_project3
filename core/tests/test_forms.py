from django.test import TestCase
from faker import Faker
from core.forms import ContatoForm


class ContatoFormTestCase(TestCase):

    def setUp(self):
        self.fake = Faker('pt_BR')


    def test_send_valid_mail(self):
        dados = {
            'nome': self.fake.name(),
            'email': self.fake.email(),
            'assunto': self.fake.sentence(),
            'mensagem': self.fake.text(max_nb_chars=100)
        }
        form = ContatoForm(data=dados)

        self.assertTrue(form.is_valid())
        self.assertTrue(form.send_mail())

    
    def test_send_invalid_mail(self):
        dados = {
            'nome': self.fake.name(),
            'email': "",
            'assunto': self.fake.sentence(),
            'mensagem': self.fake.text(max_nb_chars=100)
        }
        form = ContatoForm(data=dados)

        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)
        self.assertEqual(form.errors['email'], ['Este campo é obrigatório.'])
        