# Generated by Django 3.0.7 on 2021-01-24 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0013_auto_20210124_1849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pesan',
            name='jumlah_order',
            field=models.IntegerField(error_messages={'invalid': 'Masukan jumlah dengan benar'}),
        ),
    ]