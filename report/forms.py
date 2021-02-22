from django import forms
from django.forms import ModelForm
from report.models import report
from crispy_forms.helper import FormHelper
class ReportForm(ModelForm):
    class Meta:
        model = report
        fields = ('akun_reported', 'kodeorder_report', 'noted_report', 'upload_foto')
        widgets = {
            'akun_reported':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nama Akun Dilaporkan', 'style':'border-radius:20px;'}),
            'kodeorder_report':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Kode Order', 'style':'border-radius:20px;'}),
            'noted_report':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Catatan Laporan', 'style':'border-radius:20px;'}),
        }
        # error_messages = {
        #     'upload_foto': {
        #         'required': 'Silahkan diisi dengan lengkap',
        #     },
        #     'akun_reported': {
        #         'required': 'Silahkan diisi dengan lengkap',
        #     },
        #     'akun_reported': {
        #         'required': 'Silahkan diisi dengan lengkap',
        #     },
        # }
    def __init__(self, *args, **kwargs):
        super(ReportForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_show_labels = False