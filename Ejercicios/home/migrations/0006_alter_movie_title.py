# Generated by Django 4.1.7 on 2023-03-29 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_actor_status_alter_director_date_of_death'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='title',
            field=models.CharField(max_length=128),
        ),
    ]
