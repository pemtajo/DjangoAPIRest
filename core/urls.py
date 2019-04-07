from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^pizzaorders/$', views.PizzaOrderList.as_view(), name='pizza-order-list'),
]