# Generated by Django 5.0 on 2023-12-15 14:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tarefas", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="funcionario",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="tarefa",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
