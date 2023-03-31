# Generated by Django 4.1.7 on 2023-03-29 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_alter_movie_budget_alter_movie_profits'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='budget',
            field=models.IntegerField(blank=True, default=100000000, help_text='Escribe el presupuesto usado en esta pelicula.'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='profits',
            field=models.IntegerField(blank=True, default=300000000, help_text='Escribe las ganancias de esta pelicula.'),
        ),
    ]