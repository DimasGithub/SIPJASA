from django.shortcuts import render, redirect
from report.forms import ReportForm
from order.models import pesan
from report.models import report
from django.contrib import messages
import uuid
from django.forms import ValidationError
def indexreport(request):
    form = ReportForm(request.POST, request.FILES)
    if request.user.is_anonymous:
        request.session['alert_login'] = True
        return redirect('login:indexlogin')
    else:
        group = request.user.groups.filter(user=request.user)[0]
        if group.name == "Admin":
            return redirect('administrator:indexadmin')
        elif group.name == "Banned":
            return redirect('indexbanned')
        else :
            pass
        if request.method == "POST":
            if form.is_valid():
                try:
                    akun_reporting = request.user
                    akun_reported = request.POST.get('akun_reported')
                    kodeorder_report = str(request.POST.get('kodeorder_report'))
                    noted_report = request.POST.get('noted_report')
                    upload = request.FILES.get('upload_foto')
                    nomor = pesan.objects.get(kode= kodeorder_report)
                    if akun_reported == nomor.akun_pemesan:
                        telp_reported = nomor.telp_order
                        status_report = "Pending"
                    elif akun_reported == nomor.akun_provider:
                        telp_reported = nomor.providertelp
                        print(telp_reported)
                        status_report = "Pending"
                    else:
                        akun_reporting = "Laporan tidak valid"
                        akun_reported = "Laporan tidak valid"
                        kodeorder_report = "Laporan tidak valid"
                        noted_report = "Laporan tidak valid"
                        telp_reported="Tidak valid"
                        status_report = "Tidak valid"
                    data = report(akun_reporting=akun_reporting, akun_reported=akun_reported, kodeorder_report=kodeorder_report, noted_report=noted_report, upload_foto=upload, status_report=status_report, telp_reported=telp_reported)
                    data.save()
                    messages.success(request,'Anda berhasil melakukan report akun')
                    return redirect('index')
                except ValidationError:
                    messages.error(request, 'Kode pemesanan anda salah')
                    return redirect('index')
                except pesan.DoesNotExist:
                    messages.error(request,'Kode pemesanan yang anda masukan tidak terdaftar')
                    return redirect('index')
            else:
                print('gagal')

        else:
            form = ReportForm()
    context={
        'title':'Report | Sijasa',
        'header':'Akun Laporan',
        'forms':form,
    }
    return render(request, 'report/indexreport.html', context)
# Create your views here.
