# Generated by Django 3.2.3 on 2021-06-26 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Obras',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id de Obras')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre Obras')),
                ('descripcion', models.CharField(max_length=50, verbose_name='Nombre Obras')),
                ('precio', models.IntegerField(verbose_name='Precio obras')),
            ],
        ),
    ]
