# Generated by Django 3.0.7 on 2020-10-01 18:49

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kode', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('nama_order', models.CharField(max_length=30)),
                ('alamat_order', models.TextField()),
                ('jasa_order', models.CharField(max_length=50)),
                ('jumlah_order', models.IntegerField()),
                ('total_order', models.IntegerField()),
                ('tanggal_order', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(default='Pending', max_length=20)),
                ('nama_jasa', models.CharField(max_length=25)),
            ],
        ),
    ]
