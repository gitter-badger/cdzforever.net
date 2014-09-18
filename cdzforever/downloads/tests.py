# -*- coding: utf-8 -*-

from django.test import TestCase

from model_mommy import mommy

from .models import Categoria


class TestDownloads(TestCase):
    def setUp(self):
        self.categoria = mommy.make(Categoria)

    def test_categoria_create(self):
        self.assertEquals(Categoria.objects.count(), 1)
