from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'pizzaorders/$', views.PizzaOrderList.as_view(), name='pizza-order-list'),
    url(r'sizes/$', views.SizeList.as_view(), name='size-list'),
    url(r'flavors/$', views.FlavorList.as_view(), name='flavors-list'),
    url(r'adicionals/$', views.AdicionalList.as_view(), name='adicional-list'),
]