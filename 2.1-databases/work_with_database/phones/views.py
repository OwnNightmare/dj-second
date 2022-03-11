from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    if request.GET.get('sort') == 'name':
        p = Phone.objects.all().order_by('name')
    elif request.GET.get('sort') == 'min_price':
        p = Phone.objects.all().order_by('price')
    elif request.GET.get('sort') == 'max_price':
        p = Phone.objects.all().order_by('-price')
    else:
        p = Phone.objects.all()
    context = {'phones': p}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    p = Phone.objects.get(slug__exact=slug)
    context = {'phone': p}
    return render(request, template, context)
