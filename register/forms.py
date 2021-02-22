from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from register.models import UserProfile
from crispy_forms.helper import FormHelper
class ExtendedUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    class Meta:
        model = User
        fields = ('username','email','first_name', 'last_name', 'password1','password2')
        widgets ={
            'username':forms.TextInput(attrs={'class':'form-control','placeholder':'Nama Pengguna', 'style':'border-radius:20px;'}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'email','style':'border-radius:20px;'}),
            'first_name':forms.TextInput(attrs={'class':'form-control','placeholder':'First Name', 'style':'border-radius:20px;'}),
            'last_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name','style':'border-radius:20px;'}),
            'password1':forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password','style':'border-radius:20px;'}),
            'password2':forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password Confirmation', 'style':'border-radius:20px;'}),
        }
        def save(self, commit = True):
            user = super().save(commit=False)
            user.email = self.cleaned_data['email']
            user.first_name = self.cleaned_data['first_name']
            user.last_name = self.cleaned_data['last_name']
            if commit:
                user.save()
                return user
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_show_labels = False
        self.fields['first_name'].widget = forms.TextInput(attrs={
               
                'class':'form-control',
                'placeholder':'Nama awal', 
                'style':'border-radius:20px;'
            })
        self.fields['last_name'].widget = forms.TextInput(attrs={
               
                'class':'form-control',
                'placeholder':'Nama akhir', 
                'style':'border-radius:20px;'
            })
        self.fields['email'].widget = forms.EmailInput(attrs={
                
                'class':'form-control',
                'placeholder':'user@user.com', 
                'style':'border-radius:20px;'
            })
        self.fields['password1'].widget = forms.PasswordInput(attrs={
                
                'class':'form-control',
                'placeholder':'Password', 
                'style':'border-radius:20px;'
            })
        self.fields['password2'].widget = forms.PasswordInput(attrs={
                
                'class':'form-control',
                'placeholder':'Password confirmation', 
                'style':'border-radius:20px;'
            })

class UpdateUserForm(ModelForm):
    class Meta:
        model = User
        fields = ('username','email','first_name', 'last_name')
        widgets ={
            'username':forms.TextInput(attrs={'class':'form-control','placeholder':'Nama Pengguna', 'style':'border-radius:20px;'}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'email','style':'border-radius:20px;'}),
            'first_name':forms.TextInput(attrs={'class':'form-control','placeholder':'First Name', 'style':'border-radius:20px;'}),
            'last_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name','style':'border-radius:20px;'}),
        }
        def save(self, commit = True):
            user = super().save(commit=False)
            user.email = self.cleaned_data['email']
            user.first_name = self.cleaned_data['first_name']
            user.last_name = self.cleaned_data['last_name']
            if commit:
                user.save()
                return user
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_show_labels = False
                
class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ('dob','gender','status','profile_photo')
        widgets = {
        'dob':forms.DateInput(attrs={'class':'form-control','type':'date', 'style':'border-radius:20px;'}),
        'gender':forms.Select(attrs={'class':'form-control', 'style':'border-radius:20px;'}),
        'status':forms.Select(attrs={'class':'form-control', 'style':'border-radius:20px;'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_show_labels = False
        
class UpdateProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ('dob','gender','profile_photo')
        widgets = {
        'dob':forms.TextInput(attrs={'class':'form-control','type':'date', 'style':'border-radius:20px;'}),
        'gender':forms.Select(attrs={'class':'form-control', 'style':'border-radius:20px;'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_show_labels = False