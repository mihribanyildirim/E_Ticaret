from django.shortcuts import render, redirect
from .models import *
from django.db.models import Q

# Create your views here.

def index(request):
    Ürünler = Ürün.objects.all()
    kategoriler = Kategori.objects.all()
    search = ''
    if request.GET.get('search'):
        search = request.GET.get('search')
        Ürünler = Ürün.objects.filter(
            Q(isim__icontains = search) |
            Q(kategori__isim__icontains = search)
        )
    context = {
        'Ürünler': Ürünler,
        'search': search,
        'kategori': kategoriler
    }
    return render(request, 'bitirme.html', context)
def olustur(request):
    if request.method == 'POST':
        resim = request.FILES['resim']
        isim = request.POST['isim']

        ürün = Ürün.objects.create(isim = isim, resim = resim)
        ürün.save()
        return redirect('index')
    return render(request, 'olustur.html')