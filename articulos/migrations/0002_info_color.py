# Generated by Django 4.1.1 on 2022-11-21 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articulos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Info_Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=60)),
                ('informacion', models.TextField(max_length=300)),
                ('imagen', models.ImageField(upload_to='imagenes/')),
            ],
        ),
    ]
