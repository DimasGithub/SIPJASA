# Generated by Django 3.0.7 on 2020-10-13 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('provider', '0012_auto_20201013_0712'),
    ]

    operations = [
        migrations.AddField(
            model_name='scorejasa',
            name='kode_pesan',
            field=models.CharField(default='09e29e9d-fcbf-4cf9-851e-d86d8cbd4360', max_length=100),
            preserve_default=False,
        ),
    ]
