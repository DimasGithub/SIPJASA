# Generated by Django 3.0.7 on 2020-09-28 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('provider', '0003_bukajasa_jenis_jasa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bukajasa',
            name='deskripsi_jasa',
            field=models.TextField(),
        ),
    ]
