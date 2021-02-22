from django import forms

class Login(forms.Form):
    pengguna = forms.CharField(label='Username', widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Nama Pengguna", 'style':'border-radius:20px;' }), max_length=50)
    sandi = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Kata Sandi", 'style':'border-radius:20px;' }), max_length=50)