# Generated by Django 3.2.15 on 2023-05-11 19:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Secretaria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='nome_secretaria')),
                ('local', models.CharField(max_length=200, verbose_name='local_secretaria')),
            ],
        ),
        migrations.CreateModel(
            name='Universidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='nome_universidade')),
            ],
        ),
        migrations.CreateModel(
            name='Supervisor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200, verbose_name='nome_supervisor')),
                ('supervisor_id_secretaria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estagio.secretaria')),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='nome_curso')),
                ('curso_id_universidade', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='estagio.universidade')),
            ],
        ),
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200, verbose_name='nome_aluno')),
                ('contato', models.IntegerField(verbose_name='contato_aluno')),
                ('matricula', models.IntegerField(verbose_name='matricula')),
                ('data_incio', models.DateField(verbose_name='data_inicio')),
                ('data_fim', models.DateField(verbose_name='data_termino')),
                ('aluno_id_curso', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='estagio.curso')),
                ('aluno_id_secretaria', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='estagio.secretaria')),
                ('aluno_id_supervisor', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='estagio.supervisor')),
                ('aluno_id_universidade', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='estagio.universidade')),
            ],
        ),
    ]
