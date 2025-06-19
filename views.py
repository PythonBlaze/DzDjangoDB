from django.shortcuts import render, get_object_or_404
from .models import Phone

def catalog(request):
    sort_by = request.GET.get('sort', 'name') 
    order = request.GET.get('order', 'asc')   

    if sort_by == 'name':
        ordering = 'name' if order == 'asc' else '-name'
    elif sort_by == 'price':
        ordering = 'price' if order == 'asc' else '-price'
    else:
        ordering = 'name'

    phones = Phone.objects.all().order_by(ordering)
    return render(request, 'catalog.html', {'phones': phones})

def phone_detail(request, slug):
    phone = get_object_or_404(Phone, slug=slug)
    return render(request, 'phone_detail.html', {'phone': phone})
