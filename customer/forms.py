from django import forms
from django.forms import ModelForm
from order.models import pesan
from provider.models import bukajasa,postingjasa, scorejasa
from crispy_forms.helper import FormHelper

class editOrderJasaForm(ModelForm):
    class Meta:
        model = pesan
        fields = ('nama_order','telp_order','jumlah_order','kecamatan_order', 'alamat_order', 'catatan_order')
        widgets={
            'nama_order':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nama Jasa', 'style':'border-radius:20px;'}),
            'telp_order':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nama Jasa', 'style':'border-radius:20px;'}),
            'jumlah_order':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nama Jasa', 'style':'border-radius:20px;'}),
            'kecamatan_order':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nama Jasa', 'style':'border-radius:20px;'}),
            'alamat_order':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nama Jasa', 'style':'border-radius:20px;'}),
            'catatan_order':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nama Jasa', 'style':'border-radius:20px;'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_show_labels = False