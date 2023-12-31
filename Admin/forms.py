from django import forms
from Developer.models import *
from django.core.exceptions import ValidationError


class Customer_Creation_Form(forms.ModelForm):
    class Meta:
        model = Customers
        fields = ('name','mobile_number','email','address')
        labels = {
            'name': 'Customer Name',
            'mobile_number': 'Mobile Number',
            'email': 'Email', 
        }   
        
    # validatoions start     
    def clean_customer_mobile(self):
        mobile = self.cleaned_data.get('mobile_number')
        if mobile:
            if not mobile.isdigit() or len(mobile) != 10:
                raise ValidationError('Enter a valid 10 digit mobile number.')
        return mobile
    
    
class Brand_Creation_Form(forms.ModelForm):
    class Meta:
        model = Brands
        fields = ('brand',) 

class Product_Creation_Form(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('p_id', 'name', 'brand', 'description', 'p_image')
        labels = {
            'p_id': 'Product ID',
            'p_image': 'Product Image',
        }
        widgets = {
            'p_id': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'brand': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'p_image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }


class Supplier_Creation_Form(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ('name','contact_info')
        labels = {
            'name': 'Supplier Name',
            'contact_info':'Contact Information'
        }   

class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ('purchase_invoice_number', 'supplier', 'date', 'total_amount','bill')
        widgets = {
            'date': forms.TextInput(attrs={'type': 'date'}), 
        }


class PurchaseItemForm(forms.ModelForm):
    class Meta:
        model = PurchaseItem
        fields = ('product', 'quantity', 'rate', 'amount')
        widgets = {
            'quantity': forms.TextInput(attrs={'onchange': 'generate_amount()'}), 
            'rate': forms.TextInput(attrs={'onchange': 'generate_amount()'}), 
            'amount': forms.TextInput(attrs={'readonly': True}), 
        }



class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ('invoice_number', 'customer', 'date')
        widgets = {
            'date': forms.TextInput(attrs={'type': 'date'}), 
        }


class SaleItemForm(forms.ModelForm):
    class Meta:
        model = SaleItem
        fields = ( 'quantity', 'rate', 'product', 'amount')
        widgets = {
            'quantity': forms.TextInput(attrs={'onchange': 'generate_amount()'}), 
            'rate': forms.TextInput(attrs={'onchange': 'generate_amount()'}), 
            'amount': forms.TextInput(attrs={'readonly': True}), 
        }

