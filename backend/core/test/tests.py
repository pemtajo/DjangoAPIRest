from django.test import TestCase
from model_mommy import mommy
from django.utils.timezone import datetime
from core.models import PizzaOrder, Size, Flavor, Adicional
from decimal import Decimal

# Create your tests here.

class TestPizzaOrder(TestCase):
       
    def setUp(self):
        self.large=Size.objects.create(description='large', price=40.00, prepationTime=25)
        self.medium=Size.objects.create(description='medium', price=30.00, prepationTime=20)
        self.small=Size.objects.create(description='small', price=20.00, prepationTime=15)

        self.portuguesa=Flavor.objects.create(description='portuguesa', addPrepationTime=5)
        self.marquerita=Flavor.objects.create(description='marquerita', addPrepationTime=00)
        self.calabreza=Flavor.objects.create(description='calabreza', addPrepationTime=00)

        self.extraBacon=Adicional.objects.create(description='extraBacon', addPrice=03.00, addPrepationTime=5)
        self.withoutOnion=Adicional.objects.create(description='withoutOnion', addPrice=00.00, addPrepationTime=00)
        self.stuffedEdge=Adicional.objects.create(description='stuffedEdge', addPrice=05.00,  addPrepationTime=00)

    def test_pizzaOrderHappyDay(self):
        self.pizzaOrder = mommy.make(PizzaOrder, size=self.large, flavor=self.marquerita)
        self.assertTrue(isinstance(self.pizzaOrder, PizzaOrder))
        self.assertEquals(self.pizzaOrder.__str__(), "large marquerita")  
        self.assertEquals(self.pizzaOrder.totalPrice, 40)
        self.assertEquals(self.pizzaOrder.prepationTime, 25)

    def test_pizzaOrderHappyDayWithAdd(self):
        self.pizzaOrder = mommy.make(PizzaOrder, size=self.large, flavor=self.marquerita, adicionals=[self.extraBacon])
        self.assertTrue(isinstance(self.pizzaOrder, PizzaOrder))
        self.assertEquals(self.pizzaOrder.__str__(), "large marquerita")  
        self.assertEquals(self.pizzaOrder.totalPrice, 43)
        self.assertEquals(self.pizzaOrder.prepationTime, 30)

    def test_pizzaOrderHappyDayWithAdd2(self):
        self.pizzaOrder = mommy.make(PizzaOrder, size=self.large, flavor=self.portuguesa, adicionals=[self.extraBacon, self.stuffedEdge])
        self.assertTrue(isinstance(self.pizzaOrder, PizzaOrder))
        self.assertEquals(self.pizzaOrder.__str__(), "large portuguesa")  
        self.assertEquals(self.pizzaOrder.totalPrice, 48)
        self.assertEquals(self.pizzaOrder.prepationTime, 35)



