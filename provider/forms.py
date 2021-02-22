from django import forms
from django.forms import ModelForm
from provider.models import bukajasa,postingjasa, scorejasa
from crispy_forms.helper import FormHelper
class BukaJasaForm(ModelForm):
    class Meta:
        model = bukajasa
        fields = ('nama_jasa', 'pemilik_jasa', 'email_jasa','alamat','kecamatan','no_telp','deskripsi_jasa')
        widgets={  
        'nama_jasa':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nama Jasa', 'style':'border-radius:20px;'}),
        'pemilik_jasa':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nama Pemilik Jasa', 'style':'border-radius:20px;'}),
        'email_jasa':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Jasa', 'style':'border-radius:20px;'}),
        'alamat':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Alamat', 'style':'border-radius:20px;'}),
        'no_telp':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nomor Telepon', 'style':'border-radius:20px;'}),
        'kecamatan':forms.Select(attrs={'class':'form-control', 'placeholder':'Kecamatan', 'style':'border-radius:20px;'}),
        'deskripsi_jasa':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Deskripsi Jasa', 'style':'border-radius:20px;'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_show_labels = False
class PostingJasaForm(ModelForm):
    class Meta:
        model = postingjasa
        fields = ('jasa', 'harga_jasa', 'satuan_jasa','jenis_jasa','status_jasa','keterangan','upload_foto')
        widgets={
        'jasa':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nama Jasa', 'style':'border-radius:20px;'}),
        'harga_jasa':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Harga Jasa', 'style':'border-radius:20px;'}),
        'satuan_jasa':forms.Select(attrs={'class':'form-control', 'placeholder':'Satuan Jasa', 'style':'border-radius:20px;'}),
        'jenis_jasa':forms.Select(attrs={'class':'form-control', 'placeholder':'Jenis Jasa', 'style':'border-radius:20px;'}),
        'status_jasa':forms.Select(attrs={'class':'form-control', 'placeholder':'status Jasa', 'style':'border-radius:20px;' }),
        'keterangan':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Deskripsi Jasa', 'style':'border-radius:20px;'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_show_labels = False
class editBukaJasaForm(ModelForm):
    class Meta:
        model = bukajasa
        fields = ('nama_jasa', 'pemilik_jasa', 'email_jasa','alamat','kecamatan','no_telp','deskripsi_jasa')
        widgets={  
        'nama_jasa':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nama Jasa', 'style':'border-radius:20px;','readonly': 'readonly',}),
        'pemilik_jasa':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nama Pemilik Jasa', 'style':'border-radius:20px;'}),
        'email_jasa':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Jasa', 'style':'border-radius:20px;'}),
        'alamat':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Alamat', 'style':'border-radius:20px;'}),
        'no_telp':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nomor Telepon', 'style':'border-radius:20px;'}),
        'kecamatan':forms.Select(attrs={'class':'form-control', 'placeholder':'Kecamatan', 'style':'border-radius:20px;'}),
        'deskripsi_jasa':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Deskripsi Jasa', 'style':'border-radius:20px;'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_show_labels = False

        