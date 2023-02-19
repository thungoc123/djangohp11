from django.shortcuts import render
from .models import Product, Cartitems, Customer, Cart
from django.http import JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import json


# Create your views here.
def store(request):
  
    products = Product.objects.all()
    paginator = Paginator(products,8)
    pageNumber = request.GET.get('page')
    try:
        products = paginator.page(pageNumber)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    return render(request,'store.html',{'products':products, 'cart':cart})

def updateCart(request):
    data = json.loads(request.body)
    productId = data["productId"]
    action = data["action"]
    product = Product.objects.get(id=productId)
    customer = request.user.customer
    cart, created = Cart.objects.get_or_create(customer=customer,completed = False)
    cartitem, created = Cartitems.objects.get_or_create(cart = cart, product = product)
    
    if action == "add":
        cartitem.quantity += 1
        cartitem.save()

    return JsonResponse("Cart Updated", safe=False)


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        cart, created = Cart.objects.get_or_create(customer=customer,completed = False)
        cartitems = cart.cartitems_set.all()
    else:
        cartitems = []
        cart = {"get_cart_total":0, "get_itemtotal": 0}
    return render(request,"cart.html",{'cartitems':cartitems, 'cart':cart})
def checkout(request):
    return render(request,'checkout.html',{})
       
def updateQuantity(request):
    data = json.loads(request.body)
    quantityFieldValue = data['qfv']
    quantityFieldProduct = data['qfp']
    product = Cartitems.objects.filter(product__name = quantityFieldProduct).last()
    product.quantity = quantityFieldValue
    product.save()
    return JsonResponse("Quantity updated", safe = False)    