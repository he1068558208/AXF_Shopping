from django.db import models

# Create your models here.
from user.models import UserModel


class Main(models.Model):
    img = models.CharField(max_length=200)
    name = models.CharField(max_length=100)
    trackid = models.CharField(max_length=16)

    class Meta:
        abstract = True

class MainWheel(Main):
    class Meta:
        db_table = 'axf_wheel'

class MainNav(Main):
    class Meta:
        db_table = 'axf_nav'

class MainMustBuy(Main):

    class Meta:
        db_table = 'axf_mustbuy'

class MainShop(Main):

    class Meta:
        db_table = 'axf_shop'

class MainShow(Main):
    categoryid = models.CharField(max_length=16)
    brandname = models.CharField(max_length=100)

    img1 = models.CharField(max_length=200)
    childcid1 = models.CharField(max_length=16)
    productid1 = models.CharField(max_length=16)
    longname1 = models.CharField(max_length=100)
    price1 = models.FloatField(default=0)
    marketprice1 = models.FloatField(default=1)

    img2 = models.CharField(max_length=200)
    childcid2 = models.CharField(max_length=16)
    productid2 = models.CharField(max_length=16)
    longname2 = models.CharField(max_length=100)
    price2 = models.FloatField(default=0)
    marketprice2 = models.FloatField(default=1)

    img3 = models.CharField(max_length=200)
    childcid3 = models.CharField(max_length=16)
    productid3 = models.CharField(max_length=16)
    longname3 = models.CharField(max_length=100)
    price3 = models.FloatField(default=0)
    marketprice3 = models.FloatField(default=1)

    class Meta:
        db_table = 'axf_mainshow'

class FoodType(models.Model):
    typeid = models.CharField(max_length=16)
    typename = models.CharField(max_length=100)
    childtypenames = models.CharField(max_length=200)
    typesort = models.IntegerField(default=1)

    class Meta:
        db_table = 'axf_foodtypes'

class Goods(models.Model):
    productid = models.CharField(max_length=16)
    productimg = models.CharField(max_length=200)
    productname = models.CharField(max_length=100)
    productlongname = models.CharField(max_length=200) # 商品的规格
    isxf = models.IntegerField(default=1)
    pmdesc = models.CharField(max_length=100)
    specifics = models.CharField(max_length=100)
    price = models.FloatField(default=0)
    marketprice = models.FloatField(default=1) # 原价
    categoryid = models.CharField(max_length=16)
    childcid = models.CharField(max_length=16)
    childcidname = models.CharField(max_length=100)
    dealerid = models.CharField(max_length=16)
    storenums = models.IntegerField(default=1)
    productnum = models.IntegerField(default=1)

    class Meta:
        db_table = 'axf_goods'


class CartModel(models.Model):
    user = models.ForeignKey(UserModel) #关联用户
    goods = models.ForeignKey(Goods) # 关联商品
    c_num = models.IntegerField(default=1) #商品的个数
    is_select = models.BooleanField(default=True) # 是否选择

    class Meta:
        db_table = 'axf_cart'

class OrderModel(models.Model):
    user = models.ForeignKey(UserModel) # 关联用户
    o_num = models.CharField(max_length=64)
    # 0代表已下单，但是未付款 ， 1已付款未发货 2已付款已发货
    o_status = models.IntegerField(default=0) # 状态
    o_create = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'axf_order'

class OrderGoodsModel(models.Model):
    goods = models.ForeignKey(Goods) #关联的商品
    order = models.ForeignKey(OrderModel) #关联的订单
    goods_num = models.IntegerField(default=1) #商品的个数

    class Meta:
        db_table = 'axf_order_goods'
