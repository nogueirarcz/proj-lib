# Generated by Django 5.1.1 on 2024-09-21 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_livro', '0004_alter_livros_data_cadastro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livros',
            name='nome_emprestado',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
