# Generated by Django 4.0.5 on 2023-09-02 19:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='agenda',
            options={'ordering': ['-pk']},
        ),
        migrations.AlterUniqueTogether(
            name='agenda',
            unique_together=set(),
        ),
    ]