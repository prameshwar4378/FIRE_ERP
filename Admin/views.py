from django.shortcuts import render,redirect, get_object_or_404
from Developer.models import *
from .forms import *
from django.contrib import messages


# Create your views here.
def dashboard(request):
    return render(request,"admin__base.html")

# Create your views here.
def manage_products(request):
    return render(request,"admin__manage_products.html")

def customers_list(request):
    records=Customers.objects.all() 
    form=Customer_Creation_Form()
    if request.method == 'POST':
        form = Customer_Creation_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'Customer Created Success')
    else:
        form = Customer_Creation_Form()
    return render(request,"admin__customers_list.html",{'form':form,'records':records})

def manage_products(request):
    records=Product.objects.all() 
    form=Product_Creation_Form()
    if request.method == 'POST':
        form = Product_Creation_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'Product Created Success')
    else:
        form = Product_Creation_Form()
    return render(request,"admin__manage_products.html",{'form':form,'records':records})

 

def delete_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    product.delete()  # Delete the product
    messages.success(request,'Product Deleted Success')
    return redirect('/admin/manage_products/')  # Redirect to a list of products or another appropriate page
 
def manage_brands(request):
    records=Brands.objects.all() 
    form=Brand_Creation_Form()
    if request.method == 'POST':
        form = Brand_Creation_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'Brand Created Success')
    else:
        form = Brand_Creation_Form()
    return render(request,"admin__manage_brands.html",{'form':form,'records':records})