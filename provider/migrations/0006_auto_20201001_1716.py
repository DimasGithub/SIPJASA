# Generated by Django 3.0.7 on 2020-10-01 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('provider', '0005_auto_20200928_1757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bukajasa',
            name='alamat',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='postingjasa',
            name='status_jasa',
            field=models.CharField(choices=[('Ada', 'Ada'), ('Sibuk', 'Sibuk')], default='ADA', max_length=10),
        ),
    ]
