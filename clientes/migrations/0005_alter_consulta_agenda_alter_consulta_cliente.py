# Generated by Django 4.0.1 on 2022-01-11 00:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('medicos', '0002_agenda_user'),
        ('clientes', '0004_consulta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consulta',
            name='agenda',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='consulta', to='medicos.agenda'),
        ),
        migrations.AlterField(
            model_name='consulta',
            name='cliente',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='consulta', to='clientes.cliente'),
        ),
    ]
