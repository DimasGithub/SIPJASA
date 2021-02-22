from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from report.models import report
from order.models import pesan
import os
from django.conf import settings
from django.http import HttpResponse, Http404
def detailorderreport(request, kode):
    if request.user.is_anonymous:
        request.session['alert_login'] = True    
        return redirect('login:indexlogin')
    else:
        group = request.user.groups.filter(user=request.user)[0]
        if group.name == "Customer":
            return redirect('customer:indexcustomer')
        elif group.name == "Provider":
            return redirect('provider:indexprovider')
        elif group.name == "Banned":
            return redirect('indexbanned')
        else :
            pass
        data = pesan.objects.get(kode=kode)
    context={
        'title':'Detail pemesanan | Sipjasa',
        'header': 'Data Informasi Pemesanan ',
        'data':data,
    }
    return render(request, 'administrator/detailorderreport.html', context)
def indexmanagepengguna(request):
    if request.user.is_anonymous:
        request.session['alert_login'] = True    
        return redirect('login:indexlogin')
    else:
        alert_account = request.session.pop('alert_account', False)
        if alert_account:
            tes = True
        else:
            tes = False
        group = request.user.groups.filter(user=request.user)[0]
        if group.name == "Customer":
            return redirect('customer:indexcustomer')
        elif group.name == "Provider":
            return redirect('provider:indexprovider')
        elif group.name == "Banned":
            return redirect('indexbanned')
        else :
            pass

        data = User.objects.all()
    context={
        'title':'Kelola Pengguna | Sipjasa',
        'header':'Data pengguna',
        'data':data,
        'tes':tes,
    }
    return render(request, 'administrator/indexmanagepengguna.html', context)   
def indexadmin(request):
    if request.user.is_anonymous:
        request.session['alert_login'] = True    
        return redirect('login:indexlogin')
    else:
        alert_account = request.session.pop('alert_account', False)
        if alert_account:
            tes = True
        else:
            tes = False
        group = request.user.groups.filter(user=request.user)[0]
        if group.name == "Customer":
            return redirect('customer:indexcustomer')
        elif group.name == "Provider":
            return redirect('provider:indexprovider')
        elif group.name == "Banned":
            return redirect('indexbanned')
        else :
            pass
    context={
        'title':'Admin | Sipjasa',

    }
    return render(request, 'administrator/indexadmin.html', context)

def indexmanagereport(request):
    if request.user.is_anonymous:
        request.session['alert_login'] = True    
        return redirect('login:indexlogin')
    else:
        group = request.user.groups.filter(user=request.user)[0]
        if group.name == "Customer":
            return redirect('customer:indexcustomer')
        elif group.name == "Provider":
            return redirect('provider:indexprovider')
        elif group.name == "Banned":
            return redirect('indexbanned')
        else :
            pass
    data = report.objects.all()
    context = {
        'title':'Kelola Laporan | Sipjasa',
        'header':'Data laporan akun',
        'data':data,
    }
    return render(request, 'administrator/managereport.html', context)

def receivedreport(request, kode):
    if request.user.is_anonymous:
        request.session['alert_login'] = True    
        return redirect('login:indexlogin')
    else:
        group = request.user.groups.filter(user=request.user)[0]
        if group.name == "Customer":
            return redirect('customer:indexcustomer')
        elif group.name == "Provider":
            return redirect('provider:indexprovider')
        elif group.name == "Banned":
            return redirect('indexbanned')
        else :
            pass
        data = report.objects.get(ids=kode)
        data.status_report = "Terima"
        data.save()
        return redirect('administrator:managereport')

def rejectedreport(request, kode):
    if request.user.is_anonymous:
        request.session['alert_login'] = True    
        return redirect('login:indexlogin')
    else:
        group = request.user.groups.filter(user=request.user)[0]
        if group.name == "Customer":
            return redirect('customer:indexcustomer')
        elif group.name == "Provider":
            return redirect('provider:indexprovider')
        elif group.name == "Banned":
            return redirect('indexbanned')
        else :
            pass
        data = report.objects.get(ids=kode)
        data.status_report = "Tolak"
        data.save()
        return redirect('administrator:managereport')
def deletereport(request, kode):
    if request.user.is_anonymous:
        request.session['alert_login'] = True    
        return redirect('login:indexlogin')
    else:
        group = request.user.groups.filter(user=request.user)[0]
        if group.name == "Customer":
            return redirect('customer:indexcustomer')
        elif group.name == "Provider":
            return redirect('provider:indexprovider')
        elif group.name == "Banned":
            return redirect('indexbanned')
        else :
            pass
        report.objects.filter(ids=kode).delete()
        return redirect('administrator:managereport')

def reportorder(request):
    if request.user.is_anonymous:
        request.session['alert_login'] = True    
        return redirect('login:indexlogin')
    else:
        group = request.user.groups.filter(user=request.user)[0]
        if group.name == "Customer":
            return redirect('customer:indexcustomer')
        elif group.name == "Provider":
            return redirect('provider:indexprovider')
        elif group.name == "Banned":
            return redirect('indexbanned')
        else :
            pass
        data=pesan.objects.all()
    context={
        'title':'Monitoring Pemesanan | Sipjasa',
        'data':data,
        'header':'Data pemesanan sistem informasi jasa',
    }
    return render(request, 'administrator/olahorder.html',context)

def accountbanned(request, nomer):
    if request.user.is_anonymous:
        request.session['alert_login'] = True    
        return redirect('login:indexlogin')
    else:
        group = request.user.groups.filter(user=request.user)[0]
        if group.name == "Customer":
            return redirect('customer:indexcustomer')
        elif group.name == "Provider":
            return redirect('provider:indexprovider')
        elif group.name == "Banned":
            return redirect('indexbanned')
        else :
            pass
        #hapus group dulu
        user = User.objects.get(id=nomer)
        user.groups.clear()
        #tambah group
        group = Group.objects.get(id=3)
        group.user_set.add(nomer)
        group.save()
        return redirect('administrator:indexadmin')

def cek(request, path):
    foto = report.objects.get(ids=path)
    return render(request, 'administrator/gambar.html', context={'gambar':foto,})
# def download(request, path):
#     file_path = os.path.join(settings.MEDIA_ROOT, path)
#     if os.path.exists(file_path):
#         with open(file_path, 'rb') as fh:
#             response = HttpResponse(fh.read(), content_type="application/vnd.png")
#             response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
#             return response
#     raise Http404

def keluar(request):
    logout(request)
    return redirect('index')

