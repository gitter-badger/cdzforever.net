# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Arquivo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('numero', models.IntegerField()),
                ('titulo', models.CharField(max_length=255)),
                ('slug', models.SlugField()),
                ('audio', models.CharField(null=True, choices=[('pt_BR', 'Português (BR)'), ('jp', 'Japonês')], max_length=10)),
                ('legenda', models.CharField(null=True, choices=[('pt_BR', 'Português (BR)'), ('en', 'Inglês')], max_length=10)),
                ('screenshot', models.ImageField(null=True, blank=True, upload_to='screenshots/')),
            ],
            options={
                'ordering': ('numero', 'titulo'),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('nome', models.CharField(max_length=255)),
                ('slug', autoslug.fields.AutoSlugField(editable=False)),
                ('episodios', models.IntegerField(verbose_name='Total de Episódios')),
                ('tipo_midia', models.CharField(choices=[('anime', 'Anime'), ('filme', 'Filme'), ('ova', 'OVA'), ('manga', 'Mangá'), ('ost', 'OST')], max_length=30)),
                ('cover', models.ImageField(null=True, upload_to='covers/')),
            ],
            options={
                'ordering': ('nome',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('tipo', models.CharField(choices=[('episodio', 'Episódio'), ('legenda', 'Legenda')], max_length=10)),
                ('url', models.URLField()),
                ('arquivo', models.ForeignKey(to='catalogo.Arquivo')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Servidor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('nome', models.CharField(max_length=90)),
                ('url', models.URLField()),
            ],
            options={
                'ordering': ('nome',),
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='link',
            name='servidor',
            field=models.ForeignKey(to='catalogo.Servidor'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='arquivo',
            name='categoria',
            field=models.ForeignKey(to='catalogo.Categoria'),
            preserve_default=True,
        ),
    ]
