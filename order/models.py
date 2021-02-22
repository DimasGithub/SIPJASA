from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.core.files.storage import FileSystemStorage
from provider.models import postingjasa
import uuid
class pesan(models.Model):
    kode = models.UUIDField(default=uuid.uuid4,  editable=False, unique=True)
    nama_order = models.CharField(max_length=30)
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
    kecamatan_order = models.CharField(max_length=30, choices=kec, )
    telp_order = models.CharField(max_length=12)
    providertelp = models.CharField(max_length=12)
    alamat_order = models.TextField()
    jasa_order = models.ForeignKey(postingjasa, on_delete=models.CASCADE)
    jumlah_order = models.IntegerField(error_messages={"invalid":"Masukan jumlah dengan benar"})
    catatan_order = models.TextField()
    total_order = models.IntegerField()
    tanggal_order = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20,default="Pending")
    fs = FileSystemStorage(location='avatar/')
    gambar_order = models.FileField(storage=fs)
    nama_jasa = models.CharField(max_length=25)
    akun_pemesan = models.CharField(max_length=25)
    akun_provider = models.CharField(max_length=25)