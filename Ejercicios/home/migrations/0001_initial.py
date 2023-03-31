# Generated by Django 4.1.7 on 2023-03-27 18:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=128)),
                ('summary', models.TextField(help_text='Escribe una descripción sobre la pelicula.', max_length=500, null=True)),
                ('release_date', models.DateField(blank=True, null=True)),
                ('budget', models.IntegerField(help_text='Escribe el presupuesto usado en esta pelicula.', max_length=16, null=True)),
                ('profits', models.IntegerField(help_text='Escribe las ganancias de esta pelicula.', max_length=16, null=True)),
                ('genre', models.ManyToManyField(to='home.genre')),
            ],
        ),
        migrations.CreateModel(
            name='Directors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('names', models.CharField(max_length=64)),
                ('surnames', models.CharField(max_length=64)),
                ('nacionality', models.CharField(max_length=32, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('date_of_death', models.DateField(blank=True, null=True, verbose_name='Died')),
                ('status', models.CharField(blank=True, choices=[('A', 'Active'), ('I', 'Inactive'), ('R', 'Retired'), ('D', 'Died')], default='A', help_text='Escribe A|I|R|D para determinar el estado de actividad del director.', max_length=1)),
                ('movies', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.movies')),
            ],
        ),
        migrations.CreateModel(
            name='Actors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('names', models.CharField(max_length=64)),
                ('surnames', models.CharField(max_length=64)),
                ('nacionality', models.CharField(max_length=32, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('date_of_death', models.DateField(blank=True, null=True, verbose_name='Died')),
                ('status', models.CharField(blank=True, choices=[('A', 'Active'), ('I', 'Inactive'), ('R', 'Retired'), ('D', 'Died')], default='A', help_text='Escribe A|I|R|D para determinar el estado de actividad del actor.', max_length=1)),
                ('movies', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.movies')),
            ],
        ),
    ]