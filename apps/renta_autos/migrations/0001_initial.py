# Generated by Django 4.0.6 on 2022-07-28 15:05

import apps.renta_autos.models
from django.db import migrations, models
import django.db.models.deletion
import mirage.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Auto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auto_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='AutoColor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='AutoModelo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='AutoTipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('fec_alta', models.DateTimeField(auto_now_add=True)),
                ('user_name', models.CharField(max_length=150)),
                ('codigo_zip', models.CharField(max_length=50)),
                ('credit_card_num', mirage.fields.EncryptedCharField(max_length=255)),
                ('credit_card_ccv', mirage.fields.EncryptedCharField(max_length=255)),
                ('cuenta_numero', models.IntegerField()),
                ('direccion', models.CharField(max_length=250)),
                ('geo_latitud', models.FloatField()),
                ('geo_longitud', models.FloatField()),
                ('color_favorito', models.CharField(max_length=100)),
                ('foto_dni', models.ImageField(blank=True, null=True, upload_to=apps.renta_autos.models.upload_to)),
                ('ip', models.CharField(max_length=15)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to=apps.renta_autos.models.upload_to)),
                ('fec_birthday', models.DateField()),
                ('compras_realizadas', models.IntegerField(blank=True, default=0, null=True)),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
                'ordering': ['fec_alta'],
            },
        ),
        migrations.CreateModel(
            name='Renta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='renta_autos.auto')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rentas', to='renta_autos.cliente')),
            ],
            options={
                'verbose_name': 'Renta',
                'verbose_name_plural': 'Rentas Realizadas',
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='auto',
            name='color',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='renta_autos.autocolor'),
        ),
        migrations.AddField(
            model_name='auto',
            name='modelo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='renta_autos.automodelo'),
        ),
        migrations.AddField(
            model_name='auto',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='renta_autos.autotipo'),
        ),
    ]
