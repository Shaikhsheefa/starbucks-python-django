from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#code related to database

class Product(models.Model):
    CAT=((1,'barista_recommends'),(2,'bestseller'),(3,'drinks'),(4,'food'),(5,'merchandise'),(6,'coffee_at_home'),(7,'ready_to_eat'),(8,'latest_offerings'),(9,'anytime'),(10,'congratulations'),(11,'thank_you'))
    name=models.CharField(max_length=50, verbose_name="product_name")
    price=models.FloatField(null=False )
    discount=models.FloatField(null=True , default=0)
    pdetails=models.CharField(max_length=100, verbose_name="product details")
    cat=models.IntegerField(verbose_name="category", choices=CAT)
    is_active=models.BooleanField(default=True , verbose_name="Available")
    pimage = models.ImageField(upload_to= 'image')
     
    def __str__(self):
        return self.name
    
    
class Handcrafted(models.Model):  
    name=models.CharField(max_length=50, verbose_name="handcrafted_name")
    pimage=models.ImageField(upload_to='image_handcrafted')
    is_active=models.BooleanField(default=True, verbose_name="Available")
    
    def __str__(self):
        return self.name 

class Latestofferings(models.Model):
    CAT=((1,'barista_recommends'),
        (2,'bestseller'),
        (3,'drinks'),
        (4,'food'),
        (5,'merchandise'),
        (6,'coffee_at_home'),
        (7,'ready_to_eat'),
        (8,'latest_offerings'),
        (9,'anytime'),
        (10,'congratulations'),
        (11,'thank_you'))
    name=models.CharField(max_length=50, verbose_name="offering_name")
    sub_details=models.CharField(max_length=100, verbose_name='offering sub_details')
    details=models.CharField(max_length=150, verbose_name="offering details")
    pimage=models.ImageField(upload_to='image_latestofferings')
    price=models.FloatField(null=False)
    is_active=models.BooleanField(default=True, verbose_name='Available')
    cat=models.IntegerField(verbose_name="category", choices=CAT)
    
    
    def __str__(self):
        return self.name 
    
    
class Bestseller(models.Model):
    CAT = ((2, 'bestseller'),)  # Corrected structure for choices
    name = models.CharField(max_length=100, verbose_name='bestseller_name')
    sub_details = models.CharField(max_length=150)
    details = models.CharField(max_length=200)
    pimage = models.ImageField(upload_to='images_bestseller')
    price = models.FloatField(null=False)
    is_active = models.BooleanField(default=True, verbose_name='Available')
    cat = models.IntegerField(verbose_name="category", choices=CAT)
    
    def __str__(self):
        return self.name

class Drink(models.Model):
    CAT=((2,'bestseller'),(3,'drinks'),)
    name=models.CharField(max_length=100)
    sub_details=models.CharField(max_length=150)
    details=models.CharField(max_length=150)
    price=models.FloatField(null=False)
    is_active=models.BooleanField(default=True, verbose_name='Available')
    cat = models.IntegerField(verbose_name="category" , choices=CAT)
    pimage=models.ImageField(upload_to='images_drinks')
    
    def __str__(self):
        return self.name
    
class Anytime(models.Model):
    name=models.CharField(max_length=100)
    details=models.CharField(max_length=200)
    is_active=models.BooleanField(default=True, verbose_name='Available')
    pimage=models.ImageField(upload_to='images_anytime')
    
    def __str__(self):
        return self.name
    
class Food(models.Model):
    CAT=((11,'Veg'),(12,'Non-veg'),(13,'Healthy'),(14,'Sweet'),(15,'Conatins Egg'),(16,'Bakery'),(17,'Cake'),(18,'Dessert'),(19,'Spicy'),)
    name=models.CharField(max_length=100)
    details=models.CharField(max_length=150)
    price=models.FloatField(null=False)
    is_active=models.BooleanField(default=True, verbose_name='Available')
    cat = models.IntegerField(verbose_name="category" , choices=CAT)
    pimage=models.ImageField(upload_to='image_food')
    
class Merchandise(models.Model):
    CAT=((5,'merchandise'),)
    name=models.CharField(max_length=100)
    details=models.CharField(max_length=150)
    price=models.FloatField(null=False)
    is_active=models.BooleanField(default=True, verbose_name='Available')
    cat = models.IntegerField(verbose_name="category" , choices=CAT)
    pimage=models.ImageField(upload_to='image_merchandise')
    
class order(models.Model):
    order_id=models.CharField(max_length=50)
    uid=models.ForeignKey(User,on_delete=models.CASCADE)
    pid=models.ForeignKey(Product,on_delete=models.CASCADE)
    qty=models.IntegerField(default=1)

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s Cart Item - {self.product.name}"