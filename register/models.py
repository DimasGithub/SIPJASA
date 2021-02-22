from django.db import models
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    dob = models.DateField()
    jk = (
        ('Laki-Laki','Laki-Laki'),
        ('Perempuan', 'Perempuan')
    )
    gender = models.CharField(max_length=10, choices=jk)
    st = (
        ('Customer', 'Pelanggan'),
        ('Provider', 'Penyedia Jasa'),
    )
    status = models.CharField(max_length=10, choices=st)
    fs = FileSystemStorage(location='avatar/')
    profile_photo = models.ImageField(upload_to='avatar/')

