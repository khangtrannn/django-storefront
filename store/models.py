from uuid import uuid4

from django.db import models
from django.core.validators import MinValueValidator
from django.conf import settings

class Promotion(models.Model):
  description = models.CharField(max_length=255)
  discount = models.FloatField()

class Collection(models.Model):
  title = models.CharField(max_length=255) 
  featured_product = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True, related_name='+')
  
  def __str__(self) -> str:
    return self.title
  
class Product(models.Model):
  title = models.CharField(max_length=255)
  slug = models.SlugField()
  description = models.TextField(null=True, blank=True)
  unit_price = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(1)])
  inventory = models.IntegerField()
  last_update = models.DateTimeField(auto_now=True)
  collection = models.ForeignKey(Collection, on_delete=models.PROTECT)
  promotions = models.ManyToManyField(Promotion, blank=True)
  
  def __str__(self) -> str:
    return self.title
  
class Customer(models.Model):
  MEMBERSHIP_B = 'B' 
  MEMBERSHIP_S = 'S'
  MEMBERSHIP_G = 'G'
  
  MEMBERSHIP_CHOICES = [
    (MEMBERSHIP_B, 'Bronze'),
    (MEMBERSHIP_S, 'Silver'),
    (MEMBERSHIP_G, 'Gold'),
  ]
  phone = models.CharField(max_length=20)
  birth_date = models.DateField(null=True, blank=True)
  membership = models.CharField(max_length=1, choices=MEMBERSHIP_CHOICES, default=MEMBERSHIP_B)
  user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  
  def __str__(self) -> str:
    return f'{self.user.first_name} {self.user.last_name}'
  
  class Meta:
    ordering = ['user__first_name', 'user__last_name']
  
class Order(models.Model):
  PAYMENT_STATUS_PENDING = 'P'
  PAYMENT_STATUS_COMPLETE = 'C'
  PAYMENT_STATUS_FAILED = 'F'
  PAYMENT_STATUS_CHOICES = [
    (PAYMENT_STATUS_PENDING, 'Pending'),
    (PAYMENT_STATUS_COMPLETE, 'Complete'),
    (PAYMENT_STATUS_FAILED, 'Failed'),
  ]
  placed_at = models.DateTimeField(auto_now_add=True)
  payment_status = models.CharField(max_length=1, choices=PAYMENT_STATUS_CHOICES, default=PAYMENT_STATUS_PENDING)
  customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
  
  class Meta:
    permissions = [
      ('cancel_order', 'Can cancel order')
    ]
  
class OrderItem(models.Model):
  # Django will create reverse relation from Order to OrderItem as orderitem_set
  order = models.ForeignKey(Order, on_delete=models.PROTECT)
  product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='order_items')
  quantity = models.PositiveIntegerField()
  unit_price = models.DecimalField(max_digits=6, decimal_places=2)
  
class Address(models.Model):
  street = models.CharField(max_length=255)
  city = models.CharField(max_length=255)
  customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
  
class Cart(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid4)
  created_at = models.DateTimeField(auto_now_add=True)
  
class CartItem(models.Model):
  cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
  product = models.ForeignKey(Product, on_delete=models.CASCADE)
  quantity = models.PositiveSmallIntegerField(
    validators=[MinValueValidator(1)]
  )
  
  class Meta:
    unique_together = [['cart', 'product']]
  
class Review(models.Model):
  product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
  name = models.CharField(max_length=255)
  description = models.TextField()
  date = models.DateTimeField(auto_now_add=True)