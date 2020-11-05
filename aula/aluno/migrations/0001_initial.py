# Generated by Django 3.0.7 on 2020-11-03 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricula', models.IntegerField(blank=True, null=True)),
                ('nome', models.CharField(max_length=50)),
                ('data_nascimento', models.DateField()),
                ('cpf', models.CharField(max_length=14, unique=True)),
            ],
        ),
    ]