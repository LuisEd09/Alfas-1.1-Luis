# Generated by Django 3.0.4 on 2020-03-27 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cancion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=59)),
                ('duracion', models.DecimalField(decimal_places=2, max_digits=4)),
                ('autor', models.CharField(max_length=99)),
                ('calificacion', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
        ),
    ]
