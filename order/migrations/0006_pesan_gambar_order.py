# Generated by Django 3.0.7 on 2020-10-05 02:11

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_pesan_catatan_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='pesan',
            name='gambar_order',
            field=models.FileField(default='', storage=django.core.files.storage.FileSystemStorage(location='avatar/'), upload_to=''),
            preserve_default=False,
        ),
    ]
