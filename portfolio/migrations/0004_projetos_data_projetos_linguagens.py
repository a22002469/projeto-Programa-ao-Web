# Generated by Django 4.0.4 on 2022-05-24 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_projetos'),
    ]

    operations = [
        migrations.AddField(
            model_name='projetos',
            name='data',
            field=models.IntegerField(default=2020, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='projetos',
            name='linguagens',
            field=models.CharField(default='java', max_length=100),
            preserve_default=False,
        ),
    ]
