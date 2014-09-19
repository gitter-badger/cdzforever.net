# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse
from django.db import models

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

from . import choices


class Categoria(models.Model):
    nome = models.CharField(max_length=255)
    slug = models.SlugField()

    episodios = models.IntegerField('Total de Episódios')

    tipo_midia = models.CharField(max_length=30, choices=choices.TIPO_MIDIA)

    cover = models.ImageField(upload_to='covers/', null=True)
    cover_thumbnail = ImageSpecField(source='cover',
                                     processors=[ResizeToFill(125, 70)],  # fix me
                                     format='JPEG',
                                     options={'quality': 60})

    def __unicode__(self):
        return '{0} - {1}'.format(self.get_tipo_midia_display(), self.nome)

    @property
    def arquivos_disponiveis(self):
        return self.arquivo_set.count()

    def get_absolute_url(self):
        return reverse('catalogo:episodios', args=[self.pk])

    class Meta:
        ordering = ('nome',)


class Arquivo(models.Model):
    categoria = models.ForeignKey(Categoria)

    numero = models.IntegerField()
    titulo = models.CharField(max_length=255)
    slug = models.SlugField()

    audio = models.CharField(max_length=10, choices=choices.AUDIO, null=True)
    legenda = models.CharField(max_length=10, choices=choices.LEGENDA,
                               null=True)

    screenshot = models.ImageField(upload_to='screenshots/', blank=True,
                                   null=True)
    screenshot_thumbnail = ImageSpecField(source='screenshot',
                                          processors=[ResizeToFill(125, 70)],
                                          format='JPEG',
                                          options={'quality': 60})

    def __unicode__(self):
        return '#{0} - {1}'.format(self.numero, self.nome)

    def get_absolute_url(self):
        return reverse('catalogo:download', args=[self.pk])

    class Meta:
        ordering = ('numero', 'titulo')


class Servidor(models.Model):
    nome = models.CharField(max_length=90)
    url = models.URLField()

    def __unicode__(self):
        return self.nome

    class Meta:
        ordering = ('nome',)


class Link(models.Model):
    tipo = models.CharField(choices=choices.TIPO_LINK, max_length=10)
    servidor = models.ForeignKey(Servidor)
    arquivo = models.ForeignKey(Arquivo)

    url = models.URLField()

    def __unicode__(self):
        return self.tipo.get_tipo_display()
