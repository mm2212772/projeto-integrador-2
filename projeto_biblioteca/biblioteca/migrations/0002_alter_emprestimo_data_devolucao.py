# Generated by Django 5.1.1 on 2024-09-29 01:41

import biblioteca.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("biblioteca", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="emprestimo",
            name="data_devolucao",
            field=models.DateField(default=biblioteca.models.get_default_return_date),
        ),
    ]