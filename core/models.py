from django.db import models

# Create your models here.

class PizzaOrder(models.Model):
    class Meta:
        db_table= 'pizza_order'

    size=models.CharField(max_length=200)
    flavor=models.CharField(max_length=200)
    extraBacon=models.BooleanField()
    withoutOnion=models.BooleanField()
    stuffedEdge=models.BooleanField()
    
    def __str__(self):
        return self.size + " " + self.flavor


    