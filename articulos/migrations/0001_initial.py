# Generated by Django 4.1.1 on 2022-11-17 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CorteMujer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio', models.CharField(max_length=60)),
                ('especificacion', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Portada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=60)),
                ('foto', models.ImageField(upload_to='imagenes/')),
            ],
        ),
    ]
