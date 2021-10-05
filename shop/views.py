from django.shortcuts import render
from .models import Produit
from django.core.paginator import Paginator

def index(request):
    produit_object=Produit.objects.all()
    item_name=request.GET.get('item-name')
    if item_name!='' and item_name is not None:
        produit_object=Produit.objects.filter(nom_produit__icontains=item_name)
    paginator=Paginator(produit_object,4)
    page=request.GET.get('page')
    produit_object=paginator.get_page(page)
    return render(request,'shop/index.html',{'produit_object':produit_object})
