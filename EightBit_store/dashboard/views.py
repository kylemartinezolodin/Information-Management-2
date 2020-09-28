from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse
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
        qs_customers = Customer.objects.all()
        context = {
            'customers' : qs_customers,
            'STATUS_CHOICE' : Customer.CUSTOMER_STATUS_CHOICES
        }    
        return render(request, 'dashboard/customer.html', context)

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

        return self.get(request)
        
# REQUIRED
class DashboardProductView(View):
    def get(self, request):
        # print(Item.ITEM_TYPE_CHOICES[0][1])
        items = Item.objects.all()
        context = {
            'ITEM_TYPES':Item.ITEM_TYPE_CHOICES,
            'ITEMS':items
            }
        print(type(context['ITEM_TYPES']))
        
        return render(request, 'dashboard/products.html', context)

    def post(self, request):
        # IF addButton IS PRESENT IN POST
        if 'addButton' in request.POST:
            form = ItemForm(request.POST)

            if form.is_valid():
                itemType = request.POST.get('itemType')
                print(itemType)
                brand = request.POST.get('brand')
                itemName = request.POST.get('itemName')
                price = request.POST.get('price')

                form = Item(itemType = itemType, brand=brand, itemName=itemName, price = price)
                form.save()
                print("An Item has been added!")
            else:
                print(form.errors)
                return HttpResponse('Invalid')

        # IF updateButton IS PRESENT IN POST
        elif 'updateButton' in request.POST:
            queryId = request.POST.get('itemId')

            itemType = request.POST.get('itemType')
            brand = request.POST.get('brand')
            itemName = request.POST.get('itemName')
            price = request.POST.get('price')

            # QUERY ITEM WITH ID EQUAL TO queryId
            item = Item.objects.filter(itemId = queryId)
            # UPDATE QUERRIED ITEM
            item.update(itemType = itemType, brand=brand, itemName=itemName, price = price)
            print("An Item has been updated!")
        
        # IF deleteButton IS PRESENT IN POST
        elif 'deleteButton' in request.POST:
            queryId = request.POST.get('itemId')
            
            # QUERY ITEM WITH ID EQUAL TO queryId
            item = Item.objects.filter(itemId = queryId)
            item.delete()
            print("An Item has been updated!")
            
        return redirect('dashboard:product_view') # EXECUTE DashboardProductView.get() METHOD self.get(request)