# Generated by Django 4.0.1 on 2022-02-20 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppEntrega', '0010_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donativo',
            name='nombre',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='libros',
            name='autor',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='libros',
            name='genero',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='libros',
            name='nombre',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='apellido',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='nombre',
            field=models.CharField(max_length=50),
        ),
    ]
