from django.db import models
from django.contrib.auth.models import User

from accounting.models import Tax, Customer

class Table(models.Model):
    name = models.CharField(max_length = 150, help_text = 'Human readable name used to recognize the table')
    take_away = models.NullBooleanField(null = True, blank = True, help_text = 'Indicate if the table is used as a take away table')
    status = models.BooleanField(help_text='Enabled / Disabled')
    lock_user = models.ForeignKey(to = User, verbose_name = 'Lock to user?', null = True, blank = True)
    
class Category(models.Model):
    name = models.CharField(max_length = 150)
    status = models.BooleanField(help_text='Enabled / Disabled')

class Ingredient(models.Model):
    name = models.CharField(max_length = 150)

class IngredientReference(models.Model):
    ingredient = models.ForeignKey('Ingredient')
    dish = models.ForeignKey('Dish')
    optional = models.BooleanField(help_text='Yes / No')

class Dish(models.Model):
    name = models.CharField(max_length = 120)
    price = models.FloatField()
    category = models.ForeignKey(to = Category)
    tax = models.ForeignKey(to = Tax, blank = True, null = True)
    ingredients = models.ManyToManyField(to = Ingredient, through='IngredientReference')
    status = models.BooleanField(help_text='Enabled / Disabled')

class DishesPerOrder(models.Model):
    order = models.ForeignKey('Order')
    dish = models.ForeignKey('Dish')
    selected_ingredients = models.ManyToManyField(to = Ingredient)
    quantity = models.IntegerField()
    price = models.FloatField()

ORDER_STATUS = (
    ('op', 'Open'),
    ('pp', 'Payment Pending'),
    ('cl', 'Closed'),
)

class Order(models.Model):
    table = models.ForeignKey(to = Table)
    customer = models.ForeignKey(to = Customer)
    waiter = models.ForeignKey(to = User)
    creation_date = models.DateField(auto_now = True)
    items = models.ManyToManyField(to = Dish, through = 'DishesPerOrder')
    discount = models.FloatField(null = True, blank = True)
    taxes = models.FloatField()
    total = models.FloatField()
    status = models.CharField(max_length = 3, choices = ORDER_STATUS)