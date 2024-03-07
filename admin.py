from django.contrib import admin

from coffe_app.models import Product , Handcrafted , Latestofferings , Bestseller , Anytime , Drink , Food, Merchandise


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','name','price','cat','is_active']
    list_filter = ['cat','is_active']
    
class HandcraftedAdmin(admin.ModelAdmin):
    list_display = ['id','name','is_active']
    list_filter = ['is_active']
    
class LatestofferingsAdmin(admin.ModelAdmin):
    list_display = ['id','name','price','cat','is_active']
    list_filter =['cat','is_active']
    
class BestsellerAdmin(admin.ModelAdmin):
    list_display = ['id','name','price','cat','is_active']
    list_filter = ['cat','is_active']
    
class AnytimeAdmin(admin.ModelAdmin):
    list_display = ['id','name','is_active']
    list_filter = ['is_active']
    
class DrinkAdmin(admin.ModelAdmin):
    list_display =['id','name','price','cat','is_active']
    list_filter = ['is_active']
    
class FoodAdmmin(admin.ModelAdmin):
    list_display =['id','name','price','cat','is_active']
    list_filter = ['is_active']
    
class MerchandiseAdmin(admin.ModelAdmin):
    list_display =['id','name','price','cat','is_active']
    list_filter = ['is_active']
    
admin.site.register(Product,ProductAdmin)
admin.site.register(Handcrafted,HandcraftedAdmin)
admin.site.register(Latestofferings,LatestofferingsAdmin)
admin.site.register(Bestseller,BestsellerAdmin)
admin.site.register(Anytime,AnytimeAdmin)
admin.site.register(Drink,DrinkAdmin)
admin.site.register(Food,FoodAdmmin)
admin.site.register(Merchandise,MerchandiseAdmin)



#username (leave blank to use 'admin'): sheefa
#Email address: sheefa@gmail.com
#password: sheefa19