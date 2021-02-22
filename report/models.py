from django.db import models
from django.core.files.storage import FileSystemStorage
class report(models.Model):
    ids = models.AutoField(primary_key=True)
    akun_reporting = models.CharField(max_length=30)
    telp_reported = models.CharField(max_length=12)
    akun_reported = models.CharField(max_length=30)
    kodeorder_report = models.CharField(max_length=100)
    noted_report = models.TextField()
    datetime_report = models.DateTimeField(auto_now_add=True)
    upload_foto = models.ImageField(upload_to='avatar/')
    status_report = models.CharField(max_length=20)