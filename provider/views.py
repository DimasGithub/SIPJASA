from django.shortcuts import render, redirect, Http404
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from register.models import UserProfile
from provider.forms import BukaJasaForm, PostingJasaForm, editBukaJasaForm
from provider.models import bukajasa, postingjasa, scorejasa
from order.models import pesan
from django.contrib.auth.models import User, Group
from django.contrib import messages
def indexprovider(request):
    if request.user.is_anonymous:
        request.session['alert_login'] = True    
        return redirect('login:indexlogin')
    else:
        alert_account = request.session.pop('alert_account', False)
        if alert_account:
            tes = True
        else:
            tes = False
        alert_jasa = request.session.pop('alert_jasa', False)
        if alert_account:
            tes2 = True
        else:
            tes2 = False
        pengguna = request.user
        group = request.user.groups.filter(user=request.user)[0]
        if group.name == "Customer":
            return redirect('customer:indexcustomer')
        elif group.name == "Admin":
            return redirect('administrator:indexadmin')
        elif group.name == "Banned":
            return redirect('indexbanned')
        else :
            pass
        try:
            databukajasa = bukajasa.objects.get(user=request.user)
            gambarbukajasa = UserProfile.objects.get(user=request.user)
            context={
                'title':'Provider | sijasa',
                'header':'Selamat Datang Provider',
                'data':databukajasa,
                'gambar':gambarbukajasa,
                'alert_account':tes,
                'alert_jasa':tes2,
            }
            return render(request, 'provider/indexprovider.html', context)
        except bukajasa.DoesNotExist:
            return redirect('provider:bukajasa')
        # print(data)
        
        # cek = UserProfile.objects.filter(user=pengguna, status="Jasa")
        # print(cek)
        # if not cek:
        #     return redirect('customer:indexcustomer')
        # else:
        #     pass        

def indexbukajasa(request):
    if request.user.is_anonymous:
        request.session['alert_login'] = True    
        return redirect('login:indexlogin')
    else:
        pengguna = request.user
        # cek = UserProfile.objects.filter(user=pengguna, status="Jasa")
        # if not cek:
        #     return redirect('customer:indexcustomer')
        # else:
        #     pass
        group = request.user.groups.filter(user=request.user)[0]
        if group.name == "Customer":
            return redirect('customer:indexcustomer')
        elif group.name == "Admin":
            return redirect('administrator:indexadmin')
        elif group.name == "Banned":
            return redirect('indexbanned')
        else :
            pass
        cektoko = bukajasa.objects.filter(user=request.user)
        if not cektoko:
            if request.method == "POST":
                form = BukaJasaForm(request.POST)
                if form.is_valid():
                    form = form.save(commit=False)
                    form.user = pengguna
                    form.save()
                    return redirect('provider:indexprovider')
                else:
                    print('data buka jasa tidak valid')
            else:
                form = BukaJasaForm()
        else:
            print('sudah puya myjasa')
            request.session['alert_jasa'] = True
            return redirect('provider:indexprovider')
    context={
        'title':'Buka Jasa | Sipjasa',
        'forms':form,
        'header':'Buka myJasa',
    }
    return render(request, 'provider/bukajasa.html', context)


def editbukajasa(request):
    if request.user.is_anonymous:
        request.session['alert_login'] = True    
        return redirect('login:indexlogin')
    else:
        data = bukajasa.objects.get(user=request.user)
        dataedit = {
            'nama_jasa':data.nama_jasa,
            'pemilik_jasa':data.pemilik_jasa,
            'email_jasa':data.email_jasa,
            'alamat':data.alamat,
            'no_telp':data.no_telp,
            'kecamatan':data.kecamatan,
            'deskripsi_jasa':data.deskripsi_jasa,
            'user':request.user,
        }
        form = editBukaJasaForm(request.POST or None, request.FILES or None, initial=dataedit, instance=data)
        if request.method == "POST":
            if form.is_valid():
                form = form.save(commit=False)
                form.user = request.user
                form.save()
                messages.success(request,'Data Profil jasa berhasil diubah')
                return redirect('provider:indexprovider')
    context = {
        'title':'Edit Buka Jasa | Sipjasa',
        'header':'Ubah Data Informasi Profil Jasa',
        'forms':form,
    }
    return render(request,'provider/bukajasa.html', context)

def indexpostingjasa(request):
    if request.user.is_anonymous:
        request.session['alert_login'] = True    
        return redirect('login:indexlogin')
    else:
        pengguna = request.user
        # cek = UserProfile.objects.filter(user=pengguna, status="Jasa")
        # if not cek:
        #     return redirect('customer:indexcustomer')
        # else:
        #     pass
        group = request.user.groups.filter(user=request.user)[0]
        if group.name == "Customer":
            return redirect('customer:indexcustomer')
        elif group.name == "Admin":
            return redirect('administrator:indexadmin')
        elif group.name == "Banned":
            return redirect('indexbanned')
        else :
            pass
        try:
            namajasa = bukajasa.objects.get(user=pengguna)
            print(namajasa)
            if request.method == "POST":
                form = PostingJasaForm(request.POST, request.FILES)
                if form.is_valid():
                    form = form.save(commit=False)
                    form.nama_jasa = namajasa
                    form.save()
                    messages.success(request, 'Data jasa berhasil diposting')
                    return redirect('provider:manageposting')
                else:
                    print('postingan gagal')
            else:
                form = PostingJasaForm()
            context={
                'title':'Posting Jasa | Sipjasa',
                'header':'Posting Jasa',
                'forms':form,
            }

            return render(request, 'provider/postingjasa.html',context)
        except bukajasa.DoesNotExist:
            return redirect('provider:bukajasa')


def indexmanageposting(request):
    if request.user.is_anonymous:
        request.session['alert_login'] = True    
        return redirect('login:indexlogin')
    else:
        pengguna = request.user
        # cek = UserProfile.objects.filter(user=pengguna, status="Jasa")
        # if not cek:
        #     return redirect('customer:indexcustomer')
        # else:
        #     pass
        group = request.user.groups.filter(user=request.user)[0]
        if group.name == "Customer":
            return redirect('customer:indexcustomer')
        elif group.name == "Admin":
            return redirect('administrator:indexadmin')
        elif group.name == "Banned":
            return redirect('indexbanned')
        else :
            pass
        try:
            namajasa = bukajasa.objects.get(user=pengguna)
            tampildata = postingjasa.objects.filter(nama_jasa=namajasa)
            context={
                'title':'Kelola Posting | Sipjasa',
                'header':'Kelola Posting Jasa',
                'data':tampildata,
            }
            return render(request, 'provider/manageposting.html', context)
        except bukajasa.DoesNotExist:
            return redirect('provider:indexprovider')

def indexdeleteposting(request, id):
    if request.user.is_anonymous:
        request.session['alert_login'] = True    
        return redirect('login:indexlogin')
    else:
        pengguna = request.user
        # cek = UserProfile.objects.filter(user=pengguna, status="Jasa")
        # if not cek:
        #     return redirect('customer:indexcustomer')
        # else:
        #     pass
        group = request.user.groups.filter(user=request.user)[0]
        if group.name == "Customer":
            return redirect('customer:indexcustomer')
        elif group.name == "Admin":
            return redirect('administrator:indexadmin')
        elif group.name == "Banned":
            return redirect('indexbanned')
        else :
            pass
        data = postingjasa.objects.get(id=id).delete()
        return redirect('provider:manageposting')

def indexeditposting(request,id):
    if request.user.is_anonymous:
        request.session['alert_login'] = True    
        return redirect('login:indexlogin')
    else:
        pengguna = request.user
        # cek = UserProfile.objects.filter(user=pengguna, status="Jasa")
        # if not cek:
        #     return redirect('customer:indexcustomer')
        # else:
        #     pass
        group = request.user.groups.filter(user=request.user)[0]
        if group.name == "Customer":
            return redirect('customer:indexcustomer')
        elif group.name == "Admin":
            return redirect('administrator:indexadmin')
        elif group.name == "Banned":
            return redirect('indexbanned')
        else :
            pass
        data = postingjasa.objects.get(id=id)
        dataubah = {
            'jasa': data.jasa,
            'harga_jasa':data.harga_jasa,
            'satuan_jas':data.satuan_jasa,
            'jenis_jasa':data.jenis_jasa,
            'keterangan':data.keterangan,
            'status_jasa':data.status_jasa,
            'upload _foto':data.upload_foto,
        }
        form = PostingJasaForm(request.POST or None, request.FILES or None, initial=dataubah, instance=data)
        if request.method == "POST":
            if form.is_valid():
                form.save()
                messages.success(request,'Data posting berhasil diubah')
                return redirect('provider:manageposting')
            else:
                form = PostingJasaForm(request.POST or None, request.FILES or None, initial=dataubah, instance=data)
    context={
        'title':'Edit Posting | Sipjasa',
        'header':'Ubah Posting',
        'gambar': data,
        'data':form,
    }
    return render(request, 'provider/editposting.html', context)

def indexmanageorder(request):
    if request.user.is_anonymous:
        request.session['alert_login'] = True    
        return redirect('login:indexlogin')
    else:
        pengguna = request.user
        group = request.user.groups.filter(user=request.user)[0]
        if group.name == "Customer":
            return redirect('customer:indexcustomer')
        elif group.name == "Admin":
            return redirect('administrator:indexadmin')
        elif group.name == "Banned":
            return redirect('indexbanned')
        else :
            pass
        # cek = UserProfile.objects.filter(user=pengguna, status="Jasa")
        # if not cek:
        #     return redirect('customer:indexcustomer')
        # else:
        #     pass
        try:
            x = bukajasa.objects.get(user=pengguna)
            data = pesan.objects.filter(nama_jasa=x.nama_jasa)
            context = {
                'title' : 'Manage pemesanan | Sipjasa',
                'header': 'Data Pemesanan Jasa',
                'data':data,
            }
            return render(request, 'provider/manageorder.html', context)
        except:
            return redirect('provider:bukajasa')

def detailorder(request, kode):
    if request.user.is_anonymous:
        request.session['alert_login'] = True    
        return redirect('login:indexlogin')
    else:
        pengguna = request.user
        group = request.user.groups.filter(user=request.user)[0]
        if group.name == "Customer":
            return redirect('customer:indexcustomer')
        elif group.name == "Admin":
            return redirect('administrator:indexadmin')
        elif group.name == "Banned":
            return redirect('indexbanned')
        else :
            pass
        data = pesan.objects.get(kode=kode)
    context= {
        'title':'Detail pemesanan | Sipjasa',
        'header':'Detail Pemesanan Jasa ',
        'data':data,
    }
    return render(request, 'provider/detailorder.html', context)

def receivedorder(request, kode):
    if request.user.is_anonymous:
        request.session['alert_login'] = True    
        return redirect('login:indexlogin')
    else:
        pengguna = request.user
        group = request.user.groups.filter(user=request.user)[0]
        if group.name == "Customer":
            return redirect('customer:indexcustomer')
        elif group.name == "Admin":
            return redirect('administrator:indexadmin')
        elif group.name == "Banned":
            return redirect('indexbanned')
        else :
            pass
        # cek = UserProfile.objects.filter(user=pengguna, status="Jasa")
        # if not cek:
        #     return redirect('customer:indexcustomer')
        # else:
        #     pass
        data = pesan.objects.get(kode=kode)
        data.status = "Diterima"
        data.save()
        return redirect('provider:manageorder')

def rejectedorder(request, kode):
    if request.user.is_anonymous:
        request.session['alert_login'] = True    
        return redirect('login:indexlogin')
    else:
        pengguna = request.user
        group = request.user.groups.filter(user=request.user)[0]
        if group.name == "Customer":
            return redirect('customer:indexcustomer')
        elif group.name == "Admin":
            return redirect('administrator:indexadmin')
        elif group.name == "Banned":
            return redirect('indexbanned')
        else :
            pass
        # cek = UserProfile.objects.filter(user=pengguna, status="Jasa")
        # if not cek:
        #     return redirect('customer:indexcustomer')
        # else:
        #     pass
        data = pesan.objects.get(kode=kode)
        data.status = "Ditolak"
        data.save()
        return redirect('provider:manageorder')

def processedorder(request, kode):
    if request.user.is_anonymous:
        request.session['alert_login'] = True    
        return redirect('login:indexlogin')
    else:
        pengguna = request.user
        group = request.user.groups.filter(user=request.user)[0]
        if group.name == "Customer":
            return redirect('customer:indexcustomer')
        elif group.name == "Admin":
            return redirect('administrator:indexadmin')
        elif group.name == "Banned":
            return redirect('indexbanned')
        else :
            pass
        # cek = UserProfile.objects.filter(user=pengguna, status="Jasa")
        # if not cek:
        #     return redirect('customer:indexcustomer')
        # else:
        #     pass
        data = pesan.objects.get(kode=kode)
        data.status = "Diproses"
        data.save()
        return redirect('provider:manageorder')

def deleteorder(request, kode):
    if request.user.is_anonymous:
        request.session['alert_login'] = True    
        return redirect('login:indexlogin')
    else:
        pengguna = request.user
        group = request.user.groups.filter(user=request.user)[0]
        if group.name == "Customer":
            return redirect('customer:indexcustomer')
        elif group.name == "Admin":
            return redirect('administrator:indexadmin')
        elif group.name == "Banned":
            return redirect('indexbanned')
        else :
            pass
        # cek = UserProfile.objects.filter(user=pengguna, status="Pelanggan")
        # if not cek:
        #     return redirect('provider:indexprovider')
        # else:
        #     pass
        pesan.objects.filter(kode=kode).delete()
    return redirect('provider:manageorder')
def keluar(request):
    logout(request)
    return redirect('index')
