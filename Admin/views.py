from django.shortcuts import render,redirect, get_object_or_404
from Developer.models import *
from .forms import *
from django.contrib import messages


# Create your views here.
def dashboard(request):
    return render(request,"admin__base.html")

# Create your views here.


def erp_links(request):
    return render(request,'admin__erp_links.html')

 
def customers_list(request):
    records=Customers.objects.select_related()
    form=Customer_Creation_Form()
    if request.method == 'POST':
        form = Customer_Creation_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'Customer Created Success')
    else:
        form = Customer_Creation_Form()
    return render(request,"admin__customers_list.html",{'form':form,'records':records})


def update_customer(request,id):
    if request.method=="POST":
        pi=Customers.objects.get(pk=id)
        fm=Customer_Creation_Form(request.POST,request.FILES, instance=pi)
        if fm.is_valid():
            fm.save()
            messages.success(request,'Customer Updated Successfully')
            return redirect('/admin/customers_list/')
    else:
        pi=Customers.objects.get(pk=id)
        fm=Customer_Creation_Form(instance=pi)
    return render(request,'admin__update_customer.html',{'form':fm})


def delete_customer(request, id):
    customer = get_object_or_404(Customers, pk=id)
    customer.delete()  # Delete the product
    messages.success(request,'Customer Deleted Success')
    return redirect('/admin/customers_list/')  # Redirect to a list of products or another appropriate page


def supplier_list(request):
    records=Supplier.objects.select_related() 
    form=Supplier_Creation_Form()
    if request.method == 'POST':
        form = Supplier_Creation_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'Supplier Created Success')
    else:
        form = Supplier_Creation_Form()
    return render(request,"admin__supplier_list.html",{'form':form,'records':records})


def update_supplier(request,id):
    if request.method=="POST":
        pi=Supplier.objects.get(pk=id)
        fm=Supplier_Creation_Form(request.POST,request.FILES, instance=pi)
        if fm.is_valid():
            fm.save()
            messages.success(request,'Supplier Updated Successfully')
            return redirect('/admin/supplier_list/')
    else:
        pi=Supplier.objects.get(pk=id)
        fm=Supplier_Creation_Form(instance=pi)
    return render(request,'admin__update_supplier.html',{'form':fm})


def delete_supplier(request, id):
    supplier = get_object_or_404(Product, pk=id)
    supplier.delete()  # Delete the product
    messages.success(request,'Supplier Deleted Success')
    return redirect('/admin/supplier_list/')  # Redirect to a list of products or another appropriate page
 

def manage_products(request):
    host = request.build_absolute_uri('/')
    records=Product.objects.select_related() 
    form=Product_Creation_Form()
    if request.method == 'POST':
        form = Product_Creation_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'Product Created Success')
    else:
        form = Product_Creation_Form()
    return render(request,"admin__manage_products.html",{'form':form,'records':records,'host':host})


def update_product(request,product_id):
    if request.method=="POST":
        pi=Product.objects.get(pk=product_id)
        fm=Product_Creation_Form(request.POST,request.FILES, instance=pi)
        if fm.is_valid():
            fm.save()
            messages.success(request,'Products Updated Successfully')
            return redirect('/admin/manage_products/')
    else:
        pi=Product.objects.get(pk=product_id)
        fm=Product_Creation_Form(instance=pi)
    return render(request,'admin__update_products.html',{'form':fm})


def delete_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    product.delete()  # Delete the product
    messages.success(request,'Product Deleted Success')
    return redirect('/admin/manage_products/')  # Redirect to a list of products or another appropriate page
 
def manage_brands(request):
    records=Brands.objects.select_related() 
    form=Brand_Creation_Form()
    if request.method == 'POST':
        form = Brand_Creation_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'Brand Created Success')
    else:
        form = Brand_Creation_Form()
    return render(request,"admin__manage_brands.html",{'form':form,'records':records})


def update_brand(request,brand_id):
    if request.method=="POST":
        pi=Brands.objects.get(pk=brand_id)
        fm=Brand_Creation_Form(request.POST,request.FILES, instance=pi)
        if fm.is_valid():
            fm.save()
            messages.success(request,'Brand Updated Successfully')
            return redirect('/admin/manage_brands/')
    else:
        pi=Brands.objects.get(pk=brand_id)
        fm=Brand_Creation_Form(instance=pi)
    return render(request,'admin__update_brand.html',{'form':fm})


def delete_brand(request, brand_id):
    brand = get_object_or_404(Brands, pk=brand_id)
    brand.delete()  # Delete the brand
    messages.success(request,'Brand Deleted Success')
    return redirect('/admin/manage_brands/')  # Redirect to a list of Brands or another appropriate page
 
 
def purchase_list(request):
    records=Purchase.objects.select_related().order_by('-id')
    form=PurchaseForm()
    if request.method == 'POST':
        form = PurchaseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'Bill Added Success')
    else:
        form = PurchaseForm()
    return render(request,"admin__purchase_list.html",{'form':form,'records':records})

def update_purchase(request,id):
    if request.method=="POST":
        pi=Purchase.objects.get(pk=id)
        fm=PurchaseForm(request.POST,request.FILES, instance=pi)
        if fm.is_valid():
            fm.save()
            messages.success(request,'Bill Updated Successfully')
            return redirect('/admin/purchase_list/')
    else:
        pi=Purchase.objects.get(pk=id)
        fm=PurchaseForm(instance=pi)
    return render(request,'admin__update_purchase.html',{'form':fm})

def delete_purchase(request, id):
    purchase = get_object_or_404(Purchase, pk=id)
    purchase.delete()  # Delete the brand
    messages.success(request,'Bill Deleted Success')
    return redirect('/admin/purchase_list/')  # Redirect to a list of Brands or another appropriate page
 
 
def purchase_item_list(request, id):
    request.session['purchase_id']=id
    purchase_rec = Purchase.objects.get(id=id)
    records = PurchaseItem.objects.filter(purchase=id)
    form = PurchaseItemForm()

    if request.method == 'POST':
        form = PurchaseItemForm(request.POST, request.FILES)
        if form.is_valid():
            fm = form.save(commit=False)
            fm.purchase = purchase_rec  # Assign the Purchase instance, not the ID
            fm.save()
            messages.success(request, 'Item Added Successfully')
            id=request.session.get('purchase_id')
            return redirect(f'/admin/purchase_item_list/{id}')

    return render(request, "admin__purchase_item_list.html", {'form': form, 'records': records, 'purchase_rec': purchase_rec})


def delete_purchase_item(request, id):
    purchase_item = get_object_or_404(PurchaseItem, pk=id)
    purchase_item.delete()  # Delete the brand
    messages.success(request,'Item Deleted Success')

    id=request.session.get('purchase_id')
    return redirect(f'/admin/purchase_item_list/{id}')
 
def sale_list(request):
    records = Sale.objects.select_related().order_by('-id')
    form = SaleForm()

    if request.method == 'POST':
        form = SaleForm(request.POST, request.FILES)
        if form.is_valid():
            sale_instance = form.save()  # Save the form and get the instance
            sale_id = sale_instance.id  # Get the ID of the saved instance
            messages.success(request, 'Sale Added Successfully')
            return redirect(f'/admin/sale_item_list/{sale_id}')
    else:
        form = SaleForm()

    return render(request, "admin__sale_list.html", {'form': form, 'records': records})


def update_sale(request,id):
    if request.method=="POST":
        pi=Sale.objects.get(pk=id)
        fm=SaleForm(request.POST,request.FILES, instance=pi)
        if fm.is_valid():
            fm.save()
            messages.success(request,'Bill Updated Successfully')
            return redirect('/admin/sale_list/')
    else:
        pi=Sale.objects.get(pk=id)
        fm=SaleForm(instance=pi)
    return render(request,'admin__update_sale.html',{'form':fm})

def delete_sale(request, id):
    sale = get_object_or_404(Sale, pk=id)
    sale.delete()  # Delete the brand
    messages.success(request,'Bill Deleted Success')
    return redirect('/admin/sale_list/')  # Redirect to a list of Brands or another appropriate page


def sale_item_list(request, id):
    request.session['sale_id'] = id
    sale_rec = Sale.objects.get(id=id)
    records = SaleItem.objects.filter(sale=sale_rec)  # Filter based on the sale_rec instance
    form = SaleItemForm()
 
    if request.method == 'POST':
        form = SaleItemForm(request.POST, request.FILES)
        if form.is_valid():
            fm = form.save(commit=False)
            fm.sale = sale_rec  # Assign the Sale instance, not the ID
            fm.save()
            messages.success(request, 'Item Added Successfully')
            id = request.session.get('sale_id')
            return redirect(f'/admin/sale_item_list/{id}')

    return render(request, "admin__sale_item_list.html", {'form': form, 'records': records, 'sale_rec': sale_rec})