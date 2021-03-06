# Generated by Django 4.0.4 on 2022-05-25 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_cadeiras'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sobre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('acronimo', models.CharField(max_length=50)),
                ('ano', models.IntegerField(max_length=50)),
                ('criador', models.CharField(max_length=50)),
                ('imagem', models.ImageField(null=True, upload_to='media/')),
            ],
        ),
    ]
