# Generated by Django 4.0.4 on 2022-06-02 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0011_alter_web_nome_alter_web_noticia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='web',
            name='nome',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='web',
            name='noticia',
            field=models.CharField(max_length=1000),
        ),
    ]
