from django.test import TestCase
from faker import Faker
from core.forms import ContatoForm


class ContatoFormTestCase(TestCase):

    def setUp(self):
        fake = Faker('pt_BR')
        self.dados = {
            'nome': fake.name(),
            'email': fake.email(),
            'assunto': fake.sentence(),
            'mensagem': fake.text(max_nb_chars=100)
        }

        self.form = ContatoForm(data=self.dados)
    
    def test_send_mail(self):
        form1 = ContatoForm(data=self.dados)
        form1.is_valid()
        res1 = form1.send_mail()

        form2 = self.form
        form2.is_valid()
        res2 = form2.send_mail()

        self.assertAlmostEqual(res1,res2)