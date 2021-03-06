# Generated by Django 3.2.3 on 2021-06-26 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_obras_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Obra',
            fields=[
                ('idObra', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id Obras')),
                ('nombre_obra', models.CharField(max_length=100, verbose_name='Nombre de la Obra')),
                ('autor_obra', models.CharField(max_length=100, null=True, verbose_name='Autor')),
                ('precio', models.IntegerField(verbose_name='Valor de la Obra')),
            ],
        ),
    ]
