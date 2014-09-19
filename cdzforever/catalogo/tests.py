# -*- coding: utf-8 -*-

from django.test import TestCase

from model_mommy import mommy

from .models import Categoria, Arquivo, Servidor, Link


class CategoriaTest(TestCase):
    def setUp(self):
        self.obj = mommy.make(Categoria)

    def test_categoria_create(self):
        self.assertEquals(Categoria.objects.count(), 1)

    def test_arquivo_disponivel(self):
        self.assertEquals(self.obj.arquivos_disponiveis, 0)

        mommy.make(Arquivo, categoria=self.obj)

        self.assertEquals(self.obj.arquivos_disponiveis, 1)

        mommy.make(Arquivo, categoria=self.obj)

        self.assertEquals(self.obj.arquivos_disponiveis, 2)

    def test_categoria_repr(self):
        self.assertEquals(self.obj.__unicode__(),
                          '{0} - {1}'.format(self.obj.get_tipo_midia_display(),
                                             self.obj.nome))


class ArquivoTest(TestCase):
    def setUp(self):
        self.obj = mommy.make(Arquivo)

    def test_arquivo_create(self):
        self.assertEquals(Arquivo.objects.count(), 1)


class ServidorTest(TestCase):
    def setUp(self):
        self.obj = mommy.make(Servidor)

    def test_servidor_create(self):
        self.assertEquals(Servidor.objects.count(), 1)


class LinkTest(TestCase):
    def setUp(self):
        self.obj = mommy.make(Link)

    def test_servidor_create(self):
        self.assertEquals(Link.objects.count(), 1)
