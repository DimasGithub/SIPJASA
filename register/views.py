from django.shortcuts import render, redirect
from register.forms import ExtendedUserCreationForm, UserProfileForm, UpdateUserForm, UpdateProfileForm
from register.models import UserProfile
from django.contrib.auth.models import Group, User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
def register(request):
    if not request.user.is_anonymous:
        return redirect('index')
    else:
        pass
    form = ExtendedUserCreationForm(request.POST)
    profile_form = UserProfileForm(request.POST, request.FILES)
    if request.method == "POST":
        if form.is_valid() and profile_form.is_valid():
            status = request.POST['status']
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            user_group = Group.objects.get(name=status)
            user.groups.add(user_group)
            return redirect('login:indexlogin')
        else:
            print('data tidak valid')
    else:
        form = ExtendedUserCreationForm()
        profile_form = UserProfileForm()  
    context={
        'header':'Registrasi Akun',
        'title':'Registrasi',
        'forms': form,
        'profile_forms': profile_form,
        'message':messages,
    }
    messages.warning(request,'Sebelum registrasi baca peraturan sistem ')
    return render(request, 'register/regis.html', context)
def profilakun(request):
    if request.user.is_anonymous:
        request.session['alert_login'] = True
        return redirect('login:indexlogin')
    else:
        pass
    data1= User.objects.get(username=request.user)
    data2 = UserProfile.objects.get(user=request.user)
    data3 = request.user.groups.filter(user=request.user)[0]
    print(data3)
    context={
        'title':'Profil Akun | Sijasa',
        'header':'Profil Akun',
        'data1':data1,
        'data2':data2,
        'data3':data3,
    }
    return render(request, 'register/profil.html', context)
def editprofil(request):
    if request.user.is_anonymous:
        request.session['alert_login'] = True
        return redirect('login:indexlogin')
    else:
        pass
    profilakun = UserProfile.objects.get(user=request.user)
    if request.method == "POST":
        uformuser = UpdateUserForm(request.POST ,instance=request.user)
        uformprofile = UpdateProfileForm(request.POST , request.FILES  , instance=request.user.userprofile)
        if uformuser.is_valid() and uformprofile.is_valid():
            uformuser.save()
            uformprofile.save()
            messages.success(request,'Akun berhasil diupdate')
            return redirect('register:profilakun')
        else:
            print('gagal update')
    else:
        uformuser = UpdateUserForm(instance=request.user)
        uformprofile = UpdateProfileForm(instance=request.user.userprofile)
        context={
            'title':'Update Akun | Sijasa',
            'fUser':uformuser,
            'fProfile':uformprofile,
            'header':'Ubah Data Akun',
            'gambar':profilakun,
        }
    return render(request, 'register/editakun.html', {
            'title':'Update Akun | Sijasa',
            'fUser':uformuser,
            'fProfile':uformprofile,
            'header':'Ubah Data Akun',
            'gambar':profilakun,
        })

def change_password(request):
    if request.user.is_anonymous:
        request.session['alert_login'] = True
        return redirect('login:indexlogin')
    else:
        pass
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Kata sandi anda telah diubah')
            return redirect('register:profilakun')
        
    else:
        form = PasswordChangeForm(request.user)
    context={
        'form':form,
    }
    return render(request, 'register/changepassword.html', context)