# -*- coding: utf-8 -*-

from django.db import models

from . import choices


class Categoria(models.Model):
    nome = models.CharField(max_length=255)
    tipo_midia = models.CharField(max_length=30, choices=choices.TIPO_MIDIA)
