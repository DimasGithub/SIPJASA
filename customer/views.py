from django.shortcuts import render, redirect,get_object_or_404
from register.models import UserProfile
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from provider.models import postingjasa, bukajasa, scorejasa
from order.models import pesan
from django.core.paginator import Paginator
from django.contrib import messages
from order.forms import FormPesan
from customer.forms import editOrderJasaForm

def indexcustomer(request):
    notif = request.session.pop('notif', False)
    if notif:
        tes2 = True
    else:
        tes2 = False
    if request.user.is_anonymous:
        request.session['alert_login'] = True
        return redirect('login:indexlogin')
    else:
        pengguna = request.user
        print(pengguna)
        group = request.user.groups.filter(user=request.user)[0]
        print(group.id)
        if group.name == "Provider":
            return redirect('provider:indexprovider')
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
        search_post = request.GET.get('search')
        if search_post:
            data = postingjasa.objects.filter(Q(status_jasa="Ada", jasa__icontains=search_post))
        else:
            data = postingjasa.objects.order_by("?").filter(status_jasa="Ada")
        paginator = Paginator(data, 8)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        print(notif)
    context={
        'title':'Sipjasa',
        'page_obj':page_obj,
        'notif':tes2,
    }
    return render(request, 'customer/indexcustomer.html', context)
def indexcart(request):
    if request.user.is_anonymous:
        request.session['alert_login'] = True    
        return redirect('login:indexlogin')
    else:
        pengguna = request.user
        group = request.user.groups.filter(user=request.user)[0]
        if group.name == "Provider":
            return redirect('provider:indexprovider')
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
        data = pesan.objects.filter(akun_pemesan=pengguna)
    context = {
        'title' : 'Keranjang pemesanan | Sipjasa',
        'header': 'Data Keranjang Pemesanan',
        'data':data,
    }
    return render(request, 'customer/managecart.html', context)
def indexcartedit(request, kode):
    if request.user.is_anonymous:
        request.session['alert_login'] = True    
        return redirect('login:indexlogin')
    else:
        pengguna = request.user
        group = request.user.groups.filter(user=request.user)[0]
        if group.name == "Provider":
            return redirect('provider:indexprovider')
        elif group.name == "Admin":
            return redirect('administrator:indexadmin')
        elif group.name == "Banned":
            return redirect('indexbanned')
        else :
            pass
        data = pesan.objects.get(kode=kode)
        dataedit ={
            'kode':data.kode,
            'nama_order':data.nama_order,
            'kecamatan_order':data.kecamatan_order,
            'telp_order':data.telp_order,
            'providertelp':data.providertelp,
            'alamat_order':data.alamat_order,
            'jasa_order':data.jasa_order,
            'jumlah_order':data.jumlah_order,
            'catatan_order':data.catatan_order,
            'total_order':data.total_order,
            'tanggal_order':data.tanggal_order,
            'status_jasa':data.status,
            'gambar_order':data.gambar_order,
            'nama_jasa':data.nama_jasa,
            'akun_pemesan':data.akun_pemesan,
            'akun_provider':data.akun_provider,
        }
        if data.status == 'Pending':
            form = FormPesan(request.POST or None, initial=dataedit, instance=data)
            if request.method == "POST":
                if form.is_valid():
                    form.save()
                    messages.success(request, 'Pesanan anda berhasil diubah')
                    return redirect('customer:indexcart')
            else:
                FormPesan()
        else:
            messages.error(request, 'pesanan anda tidak dapat diubah karena status diterima / diproses')
            return redirect('customer:indexcart')
    context = {
        'title':'Ubah pesanan jasa',
        'forms':form,
        'gambar':dataedit,
        'header':'Ubah pesanan jasa',
    }
    return render(request, 'customer/editpesanan.html', context)
            
def indexcartdetail(request, kode):
    if request.user.is_anonymous:
        request.session['alert_login'] = True    
        return redirect('login:indexlogin')
    else:
        pengguna = request.user
        group = request.user.groups.filter(user=request.user)[0]
        if group.name == "Provider":
            return redirect('provider:indexprovider')
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
        data = pesan.objects.get(kode=kode)
    context= {
        'title':'Detail pemesanan | Sipjasa',
        'header':'Detail Pemesanan Jasa Anda',
        'data':data,
    }
    return render(request, 'customer/detailcart.html', context)

def deletecart(request, kode):
    if request.user.is_anonymous:
        request.session['alert_login'] = True    
        return redirect('login:indexlogin')
    else:
        pengguna = request.user
        print(pengguna)
        group = request.user.groups.filter(user=request.user)[0]
        print(group.id)
        if group.name == "Provider":
            return redirect('provider:indexprovider')
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
    return redirect('customer:indexcart')

def finishorder(request, kode):
    if request.user.is_anonymous:
        request.session['alert_login'] = True    
        return redirect('login:indexlogin')
    else:
        pengguna = request.user
        group = request.user.groups.filter(user=request.user)[0]
        if group.name == "Provider":
            return redirect('provider:indexprovider')
        elif group.name == "Admin":
            return redirect('administrator:indexadmin')
        elif group.name == "Banned":
            return redirect('indexbanned')
        else :
            pass
        data = pesan.objects.get(kode=kode)

        tes = bukajasa.objects.get(nama_jasa=data.nama_jasa)
        nilai = request.POST.get('nilai')
        ulasan = request.POST.get('ulasan')
        upload_foto = request.FILES.get('upload_foto') 
        print(tes)
        if scorejasa.objects.filter(kode_pesan=data.kode).exists():
            print('sudah dinilai')
            return redirect('customer:indexcart')
        else:
            if request.method == "POST":
                data.status = "Selesai"
                data.save() 
                nilai = scorejasa(nama_jasa=tes, nilai=nilai, jasa=data.jasa_order.jasa, nama_pelanggan=data.nama_order, kode_pesan=data.kode, ulasan=ulasan, upload_foto=upload_foto)
                nilai.save()
                messages.success(request,'Terima kasih sudah memberikan penilaian ')
                return redirect('customer:indexcart')        
    context = {
        'title':'Finish',
    }
    return render(request,'customer/score.html', context)

def keluar(request):
    logout(request)
    return redirect('index')
    