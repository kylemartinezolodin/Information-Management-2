"""EightBit_store URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from  dashboard import views
from django.views.generic import TemplateView
from dashboard.views import CustomerIndexView
import dashboard

app_name = 'dashboard'
urlpatterns = [
    path('index', views.DashboardIndexView.as_view(), name="index_view"),
    path('registration', views.DashboardOrderView.as_view(), name="order_view"),
    path('products', views.DashboardProductView.as_view(), name="product_view"),
    path('customers', views.DashboardCustomerView.as_view(), name="customer_view")
]