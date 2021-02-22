from django.db import models
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.utils.text import slugify

class bukajasa(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nama_jasa = models.CharField(max_length=25, primary_key=True)
    pemilik_jasa = models.CharField(max_length=25)
    email_jasa = models.EmailField(max_length=25)
    alamat = models.TextField()
    kec = (
        ('Bodeh', 'Bodeh'),
        ('Petarukan', 'Petarukan'),
        ('Taman', 'Taman'),
        ('Randudongkal','Randudongkal'),
        ('Ulujami', 'Ulujami'),
        ('Bantarbolang', 'Bantarbolang'),
        ('Comal', 'Comal'),
        ('Ampelgading','Ampelgading'),
        ('Watukumpul','Watukumpul'),
        ('Pemalang','Pemalang'),
        ('Belik', 'Belik'),
        ('Pulosari', 'Pulosari'),
        ('Moga', 'Moga'),
        ('Warungpring', 'Warungpring'),
    )
    kecamatan = models.CharField(max_length=25, choices=kec)
    no_telp = models.CharField(max_length=20)
    deskripsi_jasa = models.TextField()
class postingjasa(models.Model):
    nama_jasa = models.ForeignKey(bukajasa, on_delete=models.CASCADE)
    jasa = models.CharField(max_length=50)
    harga_jasa = models.IntegerField()
    units = (
        ('KG', 'KG'),
        ('KM','KM'),
        ('JAM', 'JAM'),
        ('HARI', 'HARI'),
        ('BULAN', 'BULAN'),
        ('QTY', 'QTY'),
        ('PCS', 'PCS'),
    )
    satuan_jasa = models.CharField(max_length=10, choices=units)
    js = (
        ('Pendidikan', 'Pendidikan'),
        ('Usaha Rumah Tangga', 'Usaha Rumah Tangga'),
        ('Transportasi', 'Transportasi'),
        ('Desain', 'Desain'),
        ('Teknologi', 'Teknologi'),
    )
    jenis_jasa = models.CharField(max_length=30, choices=js)
    st = (
        ('Ada', 'Ada'),
        ('Sibuk', 'Sibuk'),
    )
    status_jasa = models.CharField(max_length=10, choices=st)
    keterangan = models.TextField()
    fs = FileSystemStorage(location='avatar/')
    upload_foto = models.ImageField(upload_to = 'avatar/')

class scorejasa(models.Model):
    nama_jasa = models.ForeignKey(bukajasa, on_delete=models.CASCADE)
    nilai = models.FloatField()
    jasa = models.CharField(max_length=50)
    kode_pesan = models.CharField(max_length=100)
    nama_pelanggan = models.CharField(max_length=30)
    ulasan = models.TextField()
    upload_foto = models.ImageField(upload_to = 'avatar/', blank = True)