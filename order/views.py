from django.shortcuts import render, redirect
from provider.models import postingjasa,bukajasa, scorejasa
from order.models import pesan
from register.models import UserProfile
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from order.forms import FormPesan
def indexdetailsjasa(request, id):
    data = postingjasa.objects.get(id=id)
    tampildata = bukajasa.objects.get(nama_jasa=data.nama_jasa.nama_jasa)
    gambar = UserProfile.objects.get(user=tampildata.user.id)
    jml = scorejasa.objects.filter(nama_jasa=data.nama_jasa).count()
    average = scorejasa.objects.filter(nama_jasa=data.nama_jasa).aggregate(total=Sum('nilai')/jml)['total']
    context = {
        'title':'Details Jasa',
        'header':'Data Informasi',
        'data':tampildata,
        'gambar':gambar,
        'average':average,
    }
    return render(request, 'order/detailsjasa.html', context)
def indexdetails(request, id):
    data = postingjasa.objects.get(id=id)
    form = FormPesan(request.POST)
    ulasanjasa = scorejasa.objects.filter(nama_jasa=data.nama_jasa, jasa=data.jasa).first()
    hitung = scorejasa.objects.filter(nama_jasa=data.nama_jasa, jasa=data.jasa).count()
    if request.method == "POST":
        if request.user.is_anonymous:
            request.session['alert_login'] = True
            return redirect('login:indexlogin')
        else:
            pengguna = request.user
            group = request.user.groups.filter(user=request.user)[0]
            print(group.id)
            if group.name == "Provider":
                request.session['alert_account'] = True
                return redirect('provider:indexprovider')
            elif group.name == "Admin":
                request.session['alert_account'] = True
                return redirect('administrator:indexadmin')
            elif group.name == "Banned":
                request.session['alert_account'] = True
                return redirect('indexbanned')
            else :
                pass
            # cek = UserProfile.objects.filter(user=pengguna, status="Pelanggan")
            # if not cek:
            #     request.session['alert_account'] = True
            #     return redirect('provider:indexprovider')
            # else:
            #     pass
            
        if form.is_valid():
            nama_order = request.POST['nama_order']
            telp_order = request.POST['telp_order']
            kecamatan_order = request.POST['kecamatan_order']
            alamat_order = request.POST['alamat_order']
            catatan_order = request.POST['catatan_order']
            jumlah_order = int(request.POST['jumlah_order'])
            temp = form.save(commit=False)
            temp.akun_provider = data.nama_jasa.user
            temp.nama_jasa = data.nama_jasa.nama_jasa
            temp.providertelp = data.nama_jasa.no_telp
            temp.jasa_order = data
            temp.total_order = (jumlah_order*data.harga_jasa)
            temp.akun_pemesan = request.user
            temp.gambar_order = data.upload_foto
            temp.save()
            # akun_provider = data.nama_jasa.user
            # jasa_order = data
            # total_order = (jumlah_order*data.harga_jasa)
            # akun_pemesan = request.user
            # gambar_order = data.upload_foto
            return redirect('customer:indexcart')
        else:
            print("salah order")
    else:
        form = FormPesan()
        
    context={
        'title':'Detail | Sipjasa',
        'header':'Detail Informasi Jasa',
        'data':data,
        'form': form,
        'ulasan':ulasanjasa,
        'hitung':hitung,
    }
    return render(request, 'order/details.html', context)

def ulasan(request, id):
    data = postingjasa.objects.get(id=id)
    form = FormPesan(request.POST)
    ulasanjasa = scorejasa.objects.filter(nama_jasa=data.nama_jasa, jasa=data.jasa)
    hitung = ulasanjasa.count()
        
    context={
        'title':'Detail | Sipjasa',
        'header':'Detail Informasi Jasa',
        'data':data,
        'form': form,
        'ulasan':ulasanjasa,
        'hitung':hitung,
    }
    return render(request, 'order/ulasan.html', context)   

