from django.shortcuts import render
from django.views.generic import View
from dashboard.models import *
from dashboard.forms import *

# Create your views here.
class DashboardIndexView(View):
    def get(self, request):
        return render(request, 'dashboard/index.html')
# OPTIONAL PWEDE RA IDELETE
class DashboardOrderView(View):
    def get(self, request):
        return render(request, 'dashboard/registration.html')
    
    def post(self, request):
        customer_form = CustomerForm(request.POST)
        order_form = OrderForm(request.POST)
        cart_form = CartForm(request.POST)

        if customer_form.is_valid() and order_form.is_valid() and cart_form.is_valid():
        # CREATE CUSTOMER
            fname = request.POST.get('firstname')
            lname = request.POST.get('lastname')
            gender = request.POST.get('gender')
            contactNumber = request.POST.get('contactNumber')
            email = request.POST.get('email')

            form = Customer(firstname=fname, middlename=mname, lastname=lname, gender = gender, status = status, birthday=birthday, contactNumber= contactNumber, email=email)
            form.save()

        # CREATE ORDER
            customerId = form.customerId
            amount = request.POST.get('amount')
            orderDateTime = request.POST.get('orderDateTime')

            form = Order(customerId=customerId, amount=amount, orderDateTime=orderDateTime)
            form.save()

        # CREATE CART
            items_saved = 0
            numberOfItem = request.POST.get('numberOfItem')

            while items_saved < numberOfItem:
                orderId = form.orderId
                itemId = request.POST.get('numberOfItem' + 'items_saved')
                quantity = request.POST.get('quantity' + 'items_saved')

                form1 = Order(orderId=orderId, itemId=itemId, quantity=quantity)
                form1.save()
            

        else:
            print(form.errors)
            return HttpResponse('Invalid')

# REQUIRED
class DashboardCustomerView(View):
    def get(self, request):
        return render(request, 'dashboard/customer_registration.html')

    def post(self, request):
        form = CustomerForm(request.POST)

        if form.is_valid():
            fname = request.POST.get('firstname')
            mname = request.POST.get('middlename')
            lname = request.POST.get('lastname')
            gender = request.POST.get('gender')
            status = request.POST.get('status')
            birthday = request.POST.get('birthday')
            contactNumber = request.POST.get('contactNumber')
            email = request.POST.get('email')

            form = Customer(firstname=fname, middlename=mname, lastname=lname, gender = gender, status = status, birthday=birthday, contactNumber= contactNumber, email=email)
            form.save()
        else:
            print(form.errors)
            return HttpResponse('Invalid')
# REQUIRED
class DashboardItemView(View):
    def get(self, request):
        return render(request, 'dashboard/item_registration.html')

    def post(self, request):
        form = ItemForm(request.POST)

        if form.is_valid():
            _type = request.POST.get('_type')
            brand = request.POST.get('brand')
            itemName = request.POST.get('itemName')
            price = request.POST.get('price')

            form = Customer(_type=_type, brand=brand, itemName=itemName, price = price)
            form.save()
        else:
            print(form.errors)
            return HttpResponse('Invalid')

class CustomerIndexView(View):
    def get(self, request):
        qs_customers = Customer.objects.all()
        context = {
            'customers' : qs_customer
        }    
        return render(request, 'dashboard/customer.html', context)