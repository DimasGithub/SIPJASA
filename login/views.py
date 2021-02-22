from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from register.models import UserProfile
from login.forms import Login
from django.contrib import messages
from django.contrib.auth.models import User, Group
def indexlogin(request):
    if not request.user.is_anonymous:
        return redirect('index')
    else:
        pass
    alert_login = request.session.pop('alert_login', False)
    if alert_login:
        tes = True
    else:
        tes = False
    forms = Login(request.POST)
    username = request.POST.get('pengguna')
    password = request.POST.get('sandi')
    if request.method == "POST":
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            group = request.user.groups.filter(user=request.user)[0]
            if group.name == "Provider":
                request.session['notif'] = True
                messages.warning(request,'Baca selengkapnya tentang peraturan sistem')
                return redirect('provider:indexprovider')
            elif group.name == "Admin":
                request.session['notif'] = True
                return redirect('administrator:indexadmin')
            elif group.name == "Banned":
                request.session['notif'] = True
                return redirect('indexbanned')
            elif group.name == "Customer":
                nama = request.user
                
                request.session['notif'] = True
                alert = messages.success(request,' Selamat anda berhasil login')
                return redirect('customer:indexcustomer')
        
        else:
            messages.error(request,'Username atau password yang anda masukan salah')
            print('ga ada user')
            return redirect('login:indexlogin') 
    context ={
        'forms': forms,
        'title':'Login | Sipjasa',
        'header':'Login',
    }
    return render(request, 'login/login.html', context)