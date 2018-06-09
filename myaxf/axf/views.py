from django.http import JsonResponse
from django.shortcuts import render,HttpResponseRedirect
from axf.models import *
from django.core.urlresolvers import reverse
# Create your views here.
from user.models import UserTicketModel
from utils.functions import get_ticket


def home(request):

    if request.method =='GET':
        mainwheels = MainWheel.objects.all()
        mainnavs = MainNav.objects.all()
        mainmustbuy = MainMustBuy.objects.all()
        mainshops = MainShop.objects.all()
        mainshow = MainShow.objects.all()

        data = {
            'tittle':'首页',
            'mainwheels':mainwheels,
            'mainnav':mainnavs,
            'mainshops':mainshops,
            'mainmustbuy':mainmustbuy,
            'mainshow':mainshow,

        }

        return render(request,'home/home.html',data)

def mine(request):
    if request.method == 'GET':


        return render(request,'mine/mine.html')

def market(request):
    if request.method == 'GET':
        return HttpResponseRedirect(reverse('axf:user_market',args=('104749','0','0')))

def user_market(request, typeid, cid, sid):

    # if request.method == 'GET':
    #
    #     ticket = request.COOKIES.get('ticket')
    #     user_ticket = UserTicketModel.objects.filter(ticket=ticket).first()
    #     if user_ticket:
    #         user = user_ticket
    #     else:
    #         user = request.user

        foodtypes = FoodType.objects.all()
        if cid == '0':
            goods = Goods.objects.filter(categoryid=typeid)
        else:
            goods = Goods.objects.filter(categoryid=typeid,
                                         childcid=cid)

        foodtypes_current = foodtypes.filter(typeid=typeid).first()
        if foodtypes_current:
            childtypes = foodtypes_current.childtypenames
            childtypenames = childtypes.split('#')
            child_list = []
            for childtypename in childtypenames:
                child_type_info = childtypename.split(':')
                child_list.append(child_type_info)

        if sid == '0':
            pass
        if sid == '1':
            goods = goods.order_by('productnum')
        if sid == '2':
            goods = goods.order_by('-price')
        if sid == '3':
            goods = goods.order_by('price')

        # if user:
        #     user_cart = CartModel.objects.filter(user=user)
        # else:
        #     pass



        data = {
            'foodtypes': foodtypes,
            'goods': goods,
            'typeid':typeid,
            'child_list':child_list,
            'cid':cid
        }
        return render(request, 'market/market.html', data)

def add_cart(request):
    if request.method == 'POST':

        user = request.user
        goods_id = request.POST.get('goods_id')
        data = {
            'code':200,
            'msg':'请求成功'
        }
        if user.id:
            user_cart = CartModel.objects.filter(user=user,
                                                 goods_id=goods_id).first()
            if user_cart:
                user_cart.c_num += 1
                user_cart.save()
                data['c_num'] = user_cart.c_num
            else:
                CartModel.objects.create(user=user,
                                         goods_id=goods_id)
                data['c_num'] = 1
            return JsonResponse(data)
        data['code'] = 403
        data['msg'] = '未登录'
        return JsonResponse(data)


def sub_cart(request):
    if request.method == 'POST':
        user = request.user
        goods_id = request.POST.get('goods_id')
        data = {
            'code': 200,
            'msg': '请求成功'
        }
        if user.id:
            user_cart = CartModel.objects.filter(user=user,
                                                 goods_id=goods_id).first()
            if user_cart:
                if user_cart.c_num == 1:
                    CartModel.objects.filter(user=user,
                                             goods_id=goods_id).delete()
                    CartModel.save()
                    data['c_num'] = 0
                else:
                    user_cart.c_num -= 1
                    user_cart.save()
                    data['c_num'] = user_cart.c_num
                return JsonResponse(data)
        data['code'] = 403
        data['msg'] = '未登录'
        return JsonResponse(data)

def cart(request):
    if request.method == 'GET':
        user = request.user
        user_cart = CartModel.objects.filter(user=user)
        data = {
            'user_cart':user_cart
        }

        return render(request,'cart/cart.html',data)


def changeselect(request):

    if request.method == 'POST':
        cart_id = request.POST.get('cart_id')
        cart = CartModel.objects.filter(id=cart_id).first()
        if cart.is_select:
            cart.is_select = False
        else:
            cart.is_select = True

        data = {
            'code':200,
            'msg':'yes',
            'is_select':cart.is_select
        }
        cart.save()
        return JsonResponse(data)

def orderinfo(request):
    if request.method == 'GET':
        user = request.user
        o_num = get_ticket()
        order = OrderModel.objects.create(user=user,
                                  o_num=o_num)
        # 选择勾选商品进行下单
        user_carts = CartModel.objects.filter(user=user,is_select=True)

        for carts in user_carts:
            OrderGoodsModel.objects.create(goods=carts.goods,
                                           order=order,
                                           goods_num=carts.c_num)
        # 把已下单的商品在购物车里面删除
        user_carts.delete()
        return render(request,'order/order_info.html', {'order': order})


def changeOrderStatus(request):
    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        model = OrderModel.objects.filter(id=order_id).first()
        model.o_status = 1

        data = {
            'msg':'yes',
            'code':200
        }

        return JsonResponse(data)

