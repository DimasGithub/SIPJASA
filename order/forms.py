from django import forms
from django.forms import ModelForm
from order.models import pesan
from django.contrib.auth.forms import UserCreationForm
from crispy_forms.helper import FormHelper
class FormPesan(ModelForm):
    class Meta:
        model = pesan
        fields = ('nama_order', 'kecamatan_order', 'telp_order', 'alamat_order', 'jumlah_order', 'catatan_order')
        widgets = {
            "nama_order" : forms.TextInput(
                attrs={'class':'form-control', 'placeholder':'Nama order', 'style':'border-radius:20px;', },                
                ),
            "telp_order" : forms.TextInput(attrs={'class':'form-control', 'placeholder':'08xxxxxxxx','style':'border-radius:20px;'}),
            "jumlah_order" : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Jumlah pemesanan', 'style':'border-radius:20px;'}),     
            "kecamatan_order" : forms.Select(attrs={'class':'form-control', 'style':'border-radius:20px;'}), 
            "alamat_order" : forms.Textarea(attrs={'class':'form-control', 'placeholder':'Alamat', 'style':'border-radius:20px; height: 150px'}),
            "catatan_order" : forms.Textarea(attrs={'class':'form-control', 'placeholder':'Catatan', 'style':'border-radius:20px; height: 150px' }),
        }
        # error_messages = {
        #     'nama_order': {
        #         'required': 'Silahkan diisi dengan lengkap',
        #     },
        #     'kecamatan_order': {
        #         'required': 'Silahkan diisi dengan lengkap',
        #     },
        #     'telp_order': {
        #         'required': 'Silahkan diisi dengan lengkap',
        #     },
        #     'alamat_order': {
        #         'required': 'Silahkan diisi dengan lengkap',
        #     },
        #     'jumlah_order': {
        #         'required': 'Silahkan diisi dengan lengkap',
        #         'invalid':'Masukan data dengan benar',
        #     },
        #     'catatan_order': {
        #         'required': 'Silahkan diisi dengan lengkap',
        #     },
        # }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_show_labels = False
        self.fields['jumlah_order'].help_text = "<li>satuan KM dapat menggunkan jarak tempuh untuk jumlah pemesanan</li>"
    