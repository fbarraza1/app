# Generated by Django 5.1 on 2024-08-11 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0009_tipoabrazadera_tipocruceta_tipoposte_poste'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poste',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
