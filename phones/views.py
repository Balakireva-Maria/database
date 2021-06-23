from django.shortcuts import render

from work_with_database.phones.models import Phone
phones_list =[]

def show_catalog(request):
    template = 'catalog.html'
    context = {}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phones = Phone.objects.all()
    if phones.filter(slug=True):
        phones_list.append(phones)
    context = {'phone': phones_list}
    return render(request, template, context)
