# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('tipo_midia', models.CharField(choices=[('anime', 'Anime'), ('filme', 'Filme'), ('ova', 'OVA'), ('manga', 'Mangá'), ('ost', 'OST')], max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
