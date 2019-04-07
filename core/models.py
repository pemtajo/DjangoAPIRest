from django.db import models
from datetime import datetime, date
import operator

# Create your models here.
class Size(models.Model):
    class Meta:
        db_table='size'

    description=models.CharField(max_length=20, primary_key=True)
    price=models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    prepationTime=models.IntegerField(default=0)

    def __str__(self):
        return self.description
    
class Flavor(models.Model):
    class Meta:
        db_table='flavor'

    description=models.CharField(max_length=20, primary_key=True)
    addPrepationTime=models.IntegerField(default=0)

    def __str__(self):
        return self.description

class Adicional(models.Model):
    class Meta:
        db_table='adicional'

    description=models.CharField(max_length=50, primary_key=True)

    addPrice=models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    addPrepationTime=models.IntegerField(default=0)

    def __str__(self):
        return self.description

class PizzaOrder(models.Model):
    class Meta:
        db_table= 'pizza_order'

    size=models.ForeignKey(Size, verbose_name="Size", on_delete=models.PROTECT)
    flavor=models.ForeignKey(Flavor, verbose_name="Flavor", on_delete=models.PROTECT, default =0)
    adicionals=models.ManyToManyField(Adicional, verbose_name='Adicional', blank=True, null=True, default=None)
   
    @property
    def totalPrice(self):
        return self.size.price + sum([x.addPrice for x in self.adicionals.all()])

    @property
    def prepationTime(self):
        return self.size.prepationTime+self.flavor.addPrepationTime+sum([x.addPrepationTime for x in self.adicionals.all()])

    def __str__(self):
        return self.size + " " + self.flavor



    