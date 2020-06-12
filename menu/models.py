from django.contrib.auth.models import User
from users.models import UserProfile
from django.db import models
import uuid


class Pizza(models.Model):
    size = models.CharField(max_length=20, blank=True)
    image = models.ImageField(upload_to='images', null=True)
    topping = models.CharField(max_length=20, blank=True)
    sauce = models.CharField(max_length=20, blank=True)
    uuid = models.UUIDField(default=uuid.uuid4, unique=True)

    def __str__(self):
        return self.size

class Cart(models.Model):
    #store = models.ForeignKey(Pizza, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    active = models.BooleanField(default=True)
    order_date = models.DateField(null=True)
    
    def __unicode__(self): 
        return "%s" % (self.user)
            
    def remove_from_cart(self, pizza_id):
        pizza = Pizza.objects.get(pk=pizza_id)
        try:
            preexisting_order = PizzaOrder.objects.get(pizza=pizza, cart=self)
            if preexisting_order.quantity > 1:
                preexisting_order.quantity -= 1
                preexisting_order.save()
            else:
                preexisting_order.delete()
        except PizzaOrder.DoesNotExist:
            pass

class PizzaOrder(models.Model):
	pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
	cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
	quantity = models.IntegerField(default=0)

	def __unicode__(self): 
		return "%s, %s, %s" % (self.pizza, self.cart, self.quantity)