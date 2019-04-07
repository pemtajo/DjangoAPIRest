from django.db import models

# Create your models here.
class Size(models.Model):
    class Meta:
        db_table='size'

    description=models.CharField(max_length=20, primary_key=True)
    price=models.DecimalField(max_digits=6, decimal_places=2)
    prepationTime=models.TimeField()

    def __str__(self):
        return self.description+" "+str(self.price) + " " + str(self.prepationTime)
    
class Flavor(models.Model):
    class Meta:
        db_table='flavor'

    description=models.CharField(max_length=20, primary_key=True)
    addPrepationTime=models.IntegerField()

    def __str__(self):
        return self.description+" " + str(self.addPrepationTime)

class Adicional(models.Model):
    class Meta:
        db_table='adicional'

    description=models.CharField(max_length=50, primary_key=True)

    addPrice=models.DecimalField(max_digits=6, decimal_places=2)
    addPrepationTime=models.IntegerField()

    def __str__(self):
        return self.description+" " + str(self.addPrepationTime)

class PizzaOrder(models.Model):
    class Meta:
        db_table= 'pizza_order'

    size=models.ForeignKey(Size, verbose_name="Size", on_delete=models.PROTECT)
    flavor=models.ForeignKey(Flavor, verbose_name="Flavor", on_delete=models.PROTECT)
    adicionals=models.ManyToManyField(Adicional, verbose_name='Adicional')

    totalPrice=models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    prepationTime=models.IntegerField(default=0)
    
    def __str__(self):
        return self.size + " " + self.flavor



    