# Generated by Django 4.0.6 on 2022-07-24 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0006_alter_cliente_fec_birthday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='codigo_zip',
            field=models.CharField(max_length=50),
        ),
    ]
