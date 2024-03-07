from django.shortcuts import render,redirect,HttpResponse
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login, logout
from coffe_app.models import Product , Handcrafted , Latestofferings , Bestseller , Anytime , Drink, Food, Merchandise, Cart
from django.db.models import Q
from django.contrib.auth.decorators import login_required


def home(request):
    Product1=Product.objects.all()
    Handcrafted1=Handcrafted.objects.all()
    Latestofferings1=Latestofferings.objects.all()
    
    page_names = ['bestseller.html','drinks.html','food.html']
   
    page_links =[f'/pages/{page}/' for page in page_names ]
    
    print(Latestofferings)
    print(Handcrafted)
    print(Product)
    return render(request, template_name="home.html",
                  context={"pro" : Product1 , "hand" :Handcrafted1 , "latest" : Latestofferings1, "page_links" : page_links })   #pro is key & Product1 is value we will access data with the help of key i.e pro

def gift(request):
    return render(request , 'gift.html')

def order(request):
    Bestseller1=Bestseller.objects.all()
    
    print(Bestseller)
    return render(request , template_name="order.html", context={"best" : Bestseller1})

def bestseller(request):
    Bestseller1=Bestseller.objects.all()
    
    print(Bestseller)
    return render(request , template_name="order.html", context={"best" : Bestseller1})

def drinks(request):
    Drink1=Drink.objects.all()
    print(Drink)
    
    return render(request, template_name="drinks.html", context={"drinks" : Drink1 }) 

def food(request):
    Food1=Food.objects.all()
    print(Food)
    return render(request,template_name="food.html", context={"food" : Food1})

def merchandise(request):
    Merchandise1=Merchandise.objects.all()
    print(Merchandise)
    return render(request,template_name="merchandise.html",context={"merch" : Merchandise1})


def product_details(request, pid):
    products={
        'products': {
            'products': Product.objects.all(),
            'handcrafted': Handcrafted.objects.all(),
            'latest_offerings': Latestofferings.objects.all(),
            'bestsellers': Bestseller.objects.all(),
            'drinks': Drink.objects.all(),
            'anytime': Anytime.objects.all(),
            'food': Food.objects.all(),
            'merchandise': Merchandise.objects.all()
        }
    }
    return render(request, 'product_details.html', products)

def filter(request):
    return render(request,'filter.html')

def coffeathome(request):
    return render(request,'coffeathome.html')

def readytoeat(request):
    return render(request,'readytoeat.html')
# def user_login(request):
#     if request.method == "POST":
#         uname = request.POST.get('uname')
#         upass = request.POST.get('upass')
#         context = {}
        
#         if not uname or not upass:
#             context['errmsg'] = "Fields cannot be empty"
#             return render(request, 'login.html', context)
        
#         user = authenticate(request, username=uname, password=upass)
#         if user is not None:
#             login(request, user)
#             return redirect('/home/')  # Redirect to home page after successful login
#         else:
#             context['errmsg'] = "Invalid username or password"
#             return render(request, 'login.html', context)
           
#     else:
#         return render(request, 'login.html', {})  # Empty context passed for consistency
    
    
def user_login(request):
    if request.method == "POST":
        uname = request.POST.get('uname')
        upass = request.POST.get('upass')
        context = {}
        
        if not uname or not upass:
            context['errmsg'] = "Fields cannot be empty"
            return render(request, 'login.html', context)
        
        user = authenticate(request, username=uname, password=upass)
        if user is not None:
            login(request, user)
            return redirect('/home/')  # Redirect to home page after successful login
        else:
            context['errmsg'] = "Invalid username or password"
            return render(request, 'login.html', context)
           
    elif request.user.is_authenticated:
        return redirect('/home/')  # Redirect if user is already authenticated
    else:
        return render(request, 'login.html', {})  # Render the login page

def product_details(request,pid):
    p = Product.objects.filter(id=pid)
    context={}
    context['product'] = p
    return render(request,'product_details.html',context)

def register(request):
    if request.method=="POST":
        uname=request.POST['uname']
        upass=request.POST['upass']
        ucpass=request.POST['ucpass']
        
#To provide validation to backend mandatory field
        context={}
        if uname=="" or upass=="" or ucpass=="":
            context['errmsg']="Fields cannot be empty..."
            return render(request,'register.html',context)
        elif upass != ucpass:
            context['errmsg']="Password and comfirm password didn't match "
            return render(request,'register.html',context)
        
        else:
            try:    
                u = User.objects.create(password=upass, username=uname, email=uname)
                u.set_password(upass)   # password will be created in encrypted form
                u.save()
            
                #for succesfull msg
                context['success']="User created successfully"
                return render(request,'register.html',context)
                #return HttpResponse("Data is saved successfully")
            except Exception:
                context['errmsg']="user with same username already exist"
                return render(request,'register.html',context)
            
    else:
        return render(request,'register.html')
    
def user_logout(request):
    logout(request)
    return redirect('/home/')

def cart(request):
    return render(request,'cart.html')
    
def anytime(request):
    Anytime1=Anytime.objects.all()
   
    print(Anytime)
   
    return render(request, template_name='anytime.html' , context={"any" : Anytime1})


def sample(request):
    return render(request,'sample.html')

def store(request):
    return render(request,'store.html')

def thank_you(request):
    return render(request,'thank_you.html')


def add_to_cart(request, pid):
    if request.user.is_authenticated:    
       userid = request.user.id
       u = User.objects.get(id=userid)
       p = Product.objects.get(id=pid)
       
       # Check if the item already exists in the cart
       if cart.objects.filter(uid=u, pid=p).exists():
           message = "Product already exists in the cart!"
       else:
           c = cart.objects.create(uid=u, pid=p)
           message = "Product added successfully to the cart!"

       return redirect('view_cart')  # Redirect to the cart page
    else:
       return redirect('/login')  # Redirect to the login page if user is not authenticated

@login_required
def view_cart(request):
    # Get the cart items for the authenticated user
    cart_items = Cart.objects.filter(user=request.user)
    total_items = cart_items.count()  # Count the total number of items in the cart

    context = {
        'cart_items': cart_items,
        'total_items': total_items,
    }
    return render(request, 'cart.html', context)