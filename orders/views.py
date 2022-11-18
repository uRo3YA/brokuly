from django.shortcuts import render, redirect
from products.models import Product
from django.http import JsonResponse
import json
from accounts.models import User
from .models import Order

# Create your views here.
def orders_create(request):
    if request.method == "POST":
        temp_product_list = json.loads(request.body)
        product_list = []
        total_quantity = 0
        total_price = 0
        
        user = User.objects.get(pk=request.user.pk)
        for product in temp_product_list:
            product_list.append(product)
            total_quantity += int(product['product_quantity'])
            total_price += int(product['product_subtotal'].replace(',',''))
            #해당 유저의 장바구니에 들어있는 상품들을 삭제
            user.carts.remove(Product.objects.get(pk=product['product_pk']))

        mileage= total_price//100
        Order.objects.create(
            user=request.user,
            products=json.dumps(product_list),
            total_quantity=total_quantity,
            shipping_price=2500,
            total_price=total_price,
            mileage=mileage
        )
        order = Order.objects.order_by('-pk')[0]
    else:
        print(request.method+"입니다.")

    context = {
        'status':"성공",
        'order_pk':order.pk
    }
    return JsonResponse(context)

def orders_complete(request,pk):
    order = Order.objects.get(pk=pk)
    product_list = []

    jsonDec = json.decoder.JSONDecoder()
    order_products = jsonDec.decode(order.products)
    for product in order_products:
        temp=Product.objects.get(pk=product['product_pk'])
        product_list.append({
            'pk':temp.pk,
            'title':temp.title,
            'quantity':product['product_quantity'],
            'subtotal':product['product_subtotal'],
        })
    context = {
        'order':order,
        'product_list':product_list,
    }
    return render(request, 'orders/working/order_complete.html', context) 