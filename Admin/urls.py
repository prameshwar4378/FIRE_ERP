from django.contrib import admin
from django.urls import path
from .views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', dashboard, name="dashboard"),
    path('customers_list/', customers_list, name="admin__customers_list"),
    path('manage_products/', manage_products, name="admin__manage_products"),
    path('product/<int:product_id>', delete_product, name='admin__delete_product'),
    path('manage_brands/', manage_brands, name="admin__manage_brands"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

    