# Generated by Django 4.0.4 on 2022-05-24 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quizz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('pergunta1', models.CharField(max_length=50)),
                ('pergunta2', models.CharField(max_length=50)),
                ('pergunta3', models.CharField(max_length=50)),
                ('pergunta4', models.CharField(max_length=50)),
            ],
        ),
    ]
