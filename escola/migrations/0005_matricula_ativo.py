# Generated by Django 4.1.2 on 2022-11-07 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0004_aluno_ativo'),
    ]

    operations = [
        migrations.AddField(
            model_name='matricula',
            name='ativo',
            field=models.BooleanField(default=True),
        ),
    ]
