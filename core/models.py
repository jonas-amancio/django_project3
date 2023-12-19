import uuid
from django.db import models
from stdimage import StdImageField


def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename


class Base(models.Model):
    criado = models.DateField('Criação', auto_now_add=True)
    modificado = models.DateField('Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract=True


class Servico(Base):
    
    servico = models.CharField('Serviço', max_length=100)
    descricao = models.TextField('Descrição', max_length=100)
    icone = models.ForeignKey('core.Icone', verbose_name='Ícone', on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'

    def __str__(self):
        return self.servico


class Cargo(Base):
    cargo = models.CharField('Cargo', max_length=100)

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'

    def __str__(self):
        return self.cargo


class Funcionario(Base):
    nome = models.CharField('Nome', max_length=100)
    cargo = models.ForeignKey('core.Cargo', verbose_name='Cargo', on_delete=models.SET_NULL, null=True)
    bio = models.TextField('Bio', max_length=200)
    imagem = StdImageField('Imagem', upload_to=get_file_path, variations={'thumb': {'width': 480, 'height': 480, 'crop': True}})
    facebook = models.CharField('Facebook', max_length=100, default='#')
    twitter = models.CharField('Twitter', max_length=100, default='#')
    instagram = models.CharField('Instagram', max_length=100, default='#')

    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'

    def __str__(self):
        return self.nome


class Feature(Base):
    nome = models.CharField('Nome', max_length=100)
    descricao = models.CharField('Descrição', max_length=100)
    icone = models.ForeignKey('core.Icone', verbose_name='Ícone', on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = 'Feature'
        verbose_name_plural = 'Features'
    
    def __str__(self):
        return self.nome


class Icone(Base):
    nome  = models.CharField('Nome', max_length=100)
    tag = models.CharField('Tag', max_length=20)

    class Meta:
        verbose_name = 'Ícone'
        verbose_name_plural = 'Ícones'
    
    def __str__(self):
        return self.nome
    