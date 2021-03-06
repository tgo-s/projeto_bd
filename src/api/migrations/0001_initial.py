# Generated by Django 2.1.3 on 2018-11-30 21:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apartamento',
            fields=[
                ('apartamentoId', models.AutoField(primary_key=True, serialize=False)),
                ('bloco', models.CharField(max_length=5)),
                ('andar', models.IntegerField()),
                ('numero', models.CharField(max_length=5)),
                ('tamanho', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
            options={
                'db_table': 'apartamento',
            },
        ),
        migrations.CreateModel(
            name='Dispositivo',
            fields=[
                ('dispositivoId', models.AutoField(primary_key=True, serialize=False)),
                ('marca', models.CharField(max_length=150)),
                ('modelo', models.CharField(max_length=150)),
                ('dataInstalacao', models.DateField()),
                ('apartamentoId', models.ForeignKey(db_column='apartamentoId', on_delete=django.db.models.deletion.PROTECT, to='api.Apartamento')),
            ],
            options={
                'db_table': 'dispositivo',
            },
        ),
        migrations.CreateModel(
            name='Edificio',
            fields=[
                ('edificioId', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=50)),
                ('dataConstrucao', models.DateField()),
            ],
            options={
                'db_table': 'edificio',
            },
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('enderecoId', models.AutoField(primary_key=True, serialize=False)),
                ('cidade', models.CharField(max_length=50)),
                ('estado', models.CharField(max_length=50)),
                ('bairro', models.CharField(max_length=50)),
                ('rua', models.CharField(max_length=100)),
                ('numero', models.IntegerField()),
                ('complemento', models.CharField(max_length=100)),
                ('cep', models.CharField(max_length=15)),
                ('edificioId', models.ForeignKey(db_column='edificioId', on_delete=django.db.models.deletion.PROTECT, to='api.Edificio')),
            ],
            options={
                'db_table': 'endereco',
            },
        ),
        migrations.CreateModel(
            name='Medicao',
            fields=[
                ('medicaoId', models.AutoField(primary_key=True, serialize=False)),
                ('dataMedicao', models.DateTimeField()),
                ('valorMedido', models.DecimalField(decimal_places=2, max_digits=18)),
                ('dispositivoId', models.ForeignKey(db_column='dispositivoId', on_delete=django.db.models.deletion.PROTECT, to='api.Dispositivo')),
            ],
            options={
                'db_table': 'medicao',
            },
        ),
        migrations.CreateModel(
            name='TipoMedicao',
            fields=[
                ('tipoMedicaoId', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100)),
                ('unidadeMedida', models.CharField(max_length=5)),
                ('valorPorUnidade', models.DecimalField(decimal_places=2, max_digits=7)),
            ],
            options={
                'db_table': 'tipoMedicao',
            },
        ),
        migrations.AddField(
            model_name='medicao',
            name='tipoMedicaoId',
            field=models.ForeignKey(db_column='tipoMedicaoId', on_delete=django.db.models.deletion.PROTECT, to='api.TipoMedicao'),
        ),
        migrations.AddField(
            model_name='apartamento',
            name='edificioId',
            field=models.ForeignKey(db_column='edificioId', on_delete=django.db.models.deletion.PROTECT, to='api.Edificio'),
        ),
    ]
