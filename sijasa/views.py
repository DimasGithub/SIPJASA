from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from provider.models import postingjasa, bukajasa
from django.core.paginator import Paginator
from django.contrib.auth.models import User, Group
from django.db.models import Q
def index(request):
    search_post = request.GET.get('search')
    if search_post:
        tampildata = postingjasa.objects.filter(Q(status_jasa="Ada",jasa__icontains=search_post))
    else:
        tampildata = postingjasa.objects.order_by("?").filter(status_jasa="Ada")
    paginator = Paginator(tampildata, 8)
    page_number = request.GET.get('page')
    jasaku = bukajasa.objects.order_by("?")
    page_obj = paginator.get_page(page_number)
    context = {
        'jasaku':jasaku,
        'title':'Sipjasa',
        'data':tampildata,
        'page_obj':page_obj,
    }
    return render(request, 'index.html', context)
def indexrule(request):
    context={
        'header': "Peraturan sistem",
        'title': "Peraturan sistem | sipjasa",
    }
    return render(request, 'indexrule.html', context)
def indexguide(request):
    context={
        'header': "Panduan penggunaa sistem",
        'title': "Panduan sistem | sipjasa",
    }
    return render(request, 'indexguide.html', context)
@login_required
def indexbanned(request):
    group = request.user.groups.filter(user=request.user)[0]
    if group.name == "Customer":
        return redirect('customer:indexcustomer')
    elif group.name == "Provider":
        return redirect('provider:indexprovider')
    elif group.name == "Admin":
        return redirect('administrator:indexadmin')
    else :
        pass
    context = {
        'title':'Account Banned | Sipjasa',
        'header':'Akun Anda Telah Dihentikan',
    }
    return render(request, 'indexbanned.html', context)

def indexkategori(request, kategori):
    search_post = request.GET.get('search')
    if search_post:
        tampildata = postingjasa.objects.filter(Q(status_jasa="Ada", jenis_jasa = kategori ,jasa__icontains=search_post))
    else:
        tampildata = postingjasa.objects.order_by("?").filter(status_jasa="Ada", jenis_jasa=kategori)
    paginator = Paginator(tampildata, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'title':'Sipjasa',
        'data':tampildata,
        'page_obj':page_obj,
    }
    return render(request, 'index.html', context)