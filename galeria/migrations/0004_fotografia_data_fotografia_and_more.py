# Generated by Django 4.1.5 on 2023-02-05 15:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0003_fotografia_publicada_alter_fotografia_categoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='fotografia',
            name='data_fotografia',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='fotografia',
            name='categoria',
            field=models.CharField(choices=[('PLANETA', 'Planeta'), ('ESTRELA', 'Estrela'), ('NEBULOSA', 'Nebulosa'), ('GALÁXIA', 'Galáxia')], default='', max_length=100),
        ),
    ]
