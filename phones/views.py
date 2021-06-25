from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from work_with_database.phones.models import Phone
phones_list =[]

def show_catalog(request):
    template = 'catalog.html'
    phones = Phone.object.all()
    context = {phones}
    return render(request, template, context)


def show_product(request, post_slug):
    template = 'product.html'
    phones_exist = Phone.objects.filter(lte_exists=True)
    if phones_exist:
        info = get_object_or_404(Phone, slug=post_slug)
        phones_list.append(info)
        context = {'info': phones_list}
    else:
        return HttpResponse('page_not_found')
    return render(request, template, context)
