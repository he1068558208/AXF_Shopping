from django.conf.urls import url
from axf import views

urlpatterns = [
    url(r'^home/',views.home,name='home'),
    url(r'^mine/',views.mine,name='mine'),
    url(r'^market$',views.market,name='market'),
    url(r'^market/(\d+)/(\d+)/(\d+)/',views.user_market,name='user_market'),
    url(r'^addCart/',views.add_cart,name='addCart'),
    url(r'^subCart/',views.sub_cart,name='subCart'),
    url(r'^cart/', views.cart, name='cart'),
    url(r'^changeselect/',views.changeselect,name='changeselect'),
    url(r'^orderinfo/',views.orderinfo,name='orderinfo'),
    url(r'^changeOrderStatus/',views.changeOrderStatus,name='changeOrderStatus'),


]