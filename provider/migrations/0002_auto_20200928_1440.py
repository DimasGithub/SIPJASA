# Generated by Django 3.0.7 on 2020-09-28 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('provider', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bukajasa',
            old_name='deskripsi_toko',
            new_name='deskripsi_jasa',
        ),
        migrations.RemoveField(
            model_name='bukajasa',
            name='kota',
        ),
        migrations.RemoveField(
            model_name='bukajasa',
            name='provinsi',
        ),
        migrations.AddField(
            model_name='bukajasa',
            name='kecamatan',
            field=models.CharField(choices=[('Bodeh', 'Bodeh'), ('Petarukan', 'Petarukan'), ('Taman', 'Taman'), ('Randudongkal', 'Randudongkal'), ('Ulujami', 'Ulujami'), ('Bantarbolang', 'Bantarbolang'), ('Comal', 'Comal'), ('Ampelgading', 'Ampelgading'), ('Watukumpul', 'Watukumpul'), ('Pemalang', 'Pemalang'), ('Belik', 'Belik'), ('Pulosari', 'Pulosari'), ('Moga', 'Moga'), ('Warungpring', 'Warungpring')], default='', max_length=25),
        ),
    ]
