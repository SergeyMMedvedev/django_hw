from django.shortcuts import render, redirect, get_object_or_404
from .models import Phone


def phone_sort(phones, param):
    kwargs = {}
    kwargs['reverse'] = param == 'max_price'
    kwargs['key'] = lambda phone: phone.name if param == 'name' else phone.price
    phones.sort(**kwargs)


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    phones = list(Phone.objects.all())
    sort_param = request.GET.get('sort')
    if sort_param:
        phone_sort(phones, sort_param)
    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = get_object_or_404(Phone, slug=slug)
    context = {'phone': phone}
    return render(request, template, context)
