from django.test import TestCase
from model_mommy import mommy
from django.utils.timezone import datetime
from core.models import PizzaOrder

# Create your tests here.

class TestPizzaOrder(TestCase):
       
    def test_pizzaOrderHappyDay(self):
        self.pizzaOrder = mommy.make(PizzaOrder, size='Large', flavor='Marquerita', extraBacon=True, withoutOnion=False, stuffedEdge=False)
        self.assertTrue(isinstance(self.pizzaOrder, PizzaOrder))
        self.assertEquals(self.pizzaOrder.__str__(), "Large Marquerita")

    def test_pizzaOrder_Without_Opts(self):
        self.pizzaOrder = mommy.make(PizzaOrder, size='Large', flavor='Portuguesa')
        self.assertTrue(isinstance(self.pizzaOrder, PizzaOrder))
        self.assertEquals(self.pizzaOrder.__str__(), "Large Portuguesa")




