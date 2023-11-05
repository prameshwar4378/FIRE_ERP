from django.contrib import admin
from django.urls import path
from .views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', dashboard, name="dashboard"),
    path('customers_list/', customers_list, name="admin__customers_list"),
    path('update_customer/<int:id>', update_customer, name="admin__update_customer"),
    path('delete_customer/<int:id>', delete_customer, name="admin__delete_customer"),
    path('supplier_list/', supplier_list, name="admin__supplier_list"),
    path('update_supplier/<int:id>', update_supplier, name="admin__update_supplier"),
    path('delete_supplier/<int:id>', delete_supplier, name="admin__delete_supplier"),
    path('manage_products/', manage_products, name="admin__manage_products"),
    path('delete_product/<int:product_id>', delete_product, name='admin__delete_product'),
    path('update_product/<int:product_id>', update_product, name='admin__update_product'),
    path('manage_brands/', manage_brands, name="admin__manage_brands"),
    path('delete_brand/<int:brand_id>', delete_brand, name='admin__delete_brand'),
    path('update_brand/<int:brand_id>', update_brand, name='admin__update_brand'),
    path('erp_links/', erp_links, name='admin__erp_links'),

    path('purchase_list/', purchase_list, name='admin__purchase_list'),
    path('update_purchase/<int:id>', update_purchase, name='admin__update_purchase'),
    path('delete_purchase/<int:id>', delete_purchase, name='admin__delete_purchase'),
    path('purchase_item_list/<int:id>', purchase_item_list, name='admin__purchase_item_list'),
    path('delete_purchase_item/<int:id>', delete_purchase_item, name='admin__delete_purchase_item'),

    path('sale_list/', sale_list, name='admin__sale_list'),
    path('update_sale/<int:id>', update_sale, name='admin__update_sale'),
    path('delete_sale/<int:id>', delete_sale, name='admin__delete_sale'),
    path('sale_item_list/<int:id>', sale_item_list, name='admin__sale_item_list'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

    