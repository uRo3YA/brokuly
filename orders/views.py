from django.shortcuts import render, redirect
from products.models import Product
from django.http import JsonResponse
import json
from accounts.models import User
from .models import Order
import requests
# Create your views here.
def orders_create(request):
    if request.method == "POST":
        orders = Order.objects.filter(user_id=request.user.pk, status=0)
        for i in orders:
            i.delete()
        temp_product_list = json.loads(request.body)
        product_list = []
        total_quantity = 0
        total_price = 0
        
        user = User.objects.get(pk=request.user.pk)
        for product in temp_product_list:
            product_list.append(product)
            total_quantity += int(product['product_quantity'])
            total_price += int(product['product_subtotal'])
            #해당 유저의 장바구니에 들어있는 상품들을 삭제
            # user.carts.remove(Product.objects.get(pk=product['product_pk']))
        total_price += 2500
        mileage= total_price//20
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
    return render(request, 'orders/order_complete.html', context)

def orders_detail(request, pk):
    context = {
        'test':'test',
    }
    return render(request, 'orders/order_detail.html', context)

def go_order(request, pk):
    order = Order.objects.get(pk=pk)
    product_list = []

    jsonDec = json.decoder.JSONDecoder()
    order_products = jsonDec.decode(order.products)
    for product in order_products:
        temp=Product.objects.get(pk=product['product_pk'])
        product_list.append({
            'product':temp,
            'quantity':product['product_quantity'],
            'subtotal':product['product_subtotal'],
        })
    context = {
        'order':order,
        'product_list':product_list,
    }
    return render(request, 'orders/go_order.html', context)

def pay(request, pk):
    if request.method == "POST":
        order = Order.objects.get(pk=pk)
        jsonDec = json.decoder.JSONDecoder()
        order_products = jsonDec.decode(order.products)

        URL = 'https://kapi.kakao.com/v1/payment/ready'
        headers = {
            "Authorization": "KakaoAK " + "5b0c96a50fea84174b8ae3bd9d33b084",   # 변경불가
            "Content-type": "application/x-www-form-urlencoded;charset=utf-8",  # 변경불가
        }
        params = {
            "cid": "TC0ONETIME",    # 테스트용 코드
            "partner_order_id": pk,     # 주문번호
            "partner_user_id": request.user.username,    # 유저 아이디
            "item_name": f"{Product.objects.get(pk=order_products[0]['product_pk']).title} 외 {order.total_quantity - 1} 개",        # 구매 물품 이름
            "quantity": order.total_quantity,                # 구매 물품 수량
            "total_amount": order.total_price,        # 구매 물품 가격
            "tax_free_amount": "0",         # 구매 물품 비과세
            "approval_url": f"http://brokurly.shop/orders/success/{order.pk}/",
            "cancel_url": f"http://brokurly.shop/orders/cancel/{order.pk}/",
            "fail_url": f"http://brokurly.shop/orders/fail/{order.pk}/",
        }
        
        res = requests.post(URL, headers=headers, params=params)
        # request.session['tid'] = res.json()['tid']      # 결제 승인시 사용할 tid를 세션에 저장
        order.tid = res.json()['tid']      # 결제 승인시 사용할 tid를 DB에 저장
        order.save()
        next_url = res.json()['next_redirect_pc_url']   # 결제 페이지로 넘어갈 url을 저장
        return redirect(next_url)

    else:
        print("get")

def success(request, pk):
    order = Order.objects.get(pk=pk)

    URL = 'https://kapi.kakao.com/v1/payment/approve'
    headers = {
        "Authorization": "KakaoAK " + "5b0c96a50fea84174b8ae3bd9d33b084",
        "Content-type": "application/x-www-form-urlencoded;charset=utf-8",
    }
    params = {
        "cid": "TC0ONETIME",    # 테스트용 코드
        # "tid": request.session['tid'],  # 결제 요청시 세션에 저장한 tid
        "tid": order.tid,  # 결제 요청시 세션에 저장한 tid
        "partner_order_id": pk,     # 주문번호
        "partner_user_id": request.user.username,    # 유저 아이디
        "pg_token": request.GET.get("pg_token"),     # 쿼리 스트링으로 받은 pg토큰
    }
    
    order.status = 1
    order.save()

    user = User.objects.get(pk=request.user.pk)

    jsonDec = json.decoder.JSONDecoder()
    order_products = jsonDec.decode(order.products)
    for product in order_products:
        user.carts.remove(Product.objects.get(pk=product['product_pk']))

    res = requests.post(URL, headers=headers, params=params)
    # amount = res.json()['amount']['total']
    res = res.json()
    context = {
        'res': res,
        # 'amount': amount,
    }
    # return render(request, 'orders/working/success.html', context)
    return render(request, 'orders/order_complete.html', context)

def cancel(request):
    return render(request, 'orders/cancel.html')

def fail(request):
    return render(request, 'orders/fail.html')