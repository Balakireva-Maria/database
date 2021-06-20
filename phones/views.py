from django.shortcuts import render

from work_with_database.phones.models import Phone


def show_catalog(request):
    template = 'catalog.html'
    context = {}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.all()
    context = {'phone': phone}
    return render(request, template, context)
