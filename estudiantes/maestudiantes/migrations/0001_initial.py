# Generated by Django 4.2.11 on 2024-05-11 16:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('rut', models.CharField(max_length=9, unique=True)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('fecha_nac', models.DateField()),
                ('activo', models.BooleanField(default=False)),
                ('creacion_registro', models.DateField(auto_now_add=True)),
                ('modificacion_registro', models.DateField(auto_now=True)),
                ('creado_por', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=9, unique=True)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('activo', models.BooleanField(default=False)),
                ('creacion_registro', models.DateField(auto_now_add=True)),
                ('modificacion_registro', models.DateField(auto_now=True)),
                ('creado_por', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('calle', models.CharField(max_length=50)),
                ('numero', models.CharField(max_length=10)),
                ('dpto', models.CharField(blank=True, max_length=10)),
                ('comuna', models.CharField(max_length=50)),
                ('ciudad', models.CharField(max_length=50)),
                ('region', models.CharField(max_length=50)),
                ('estudiante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maestudiantes.estudiante')),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=9, unique=True)),
                ('nombre', models.CharField(max_length=50)),
                ('version', models.IntegerField(null=True)),
                ('profesor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='maestudiantes.profesor')),
            ],
        ),
    ]