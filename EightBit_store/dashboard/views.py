from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse
from dashboard.models import *
from dashboard.forms import *
from decimal import Decimal

# Create your views here.
class DashboardIndexView(View):
    def get(self, request):
        # orders = Cart.objects.raw("SELECT `order`.orderId, customer.customerId, lastname, orderDateTime, item.itemId, itemName, price, quantity, amount FROM `cart` INNER JOIN `order` ON `order`.orderId = cart.orderId INNER JOIN item ON item.itemId = cart.itemId INNER JOIN customer ON customer.customerId = `order`.customerId")
        
        # DOES NOT SELECT ORDERS WITH THE SAME orderId
        orders = Cart.objects.raw("SELECT * FROM `cart` INNER JOIN `order` ON `order`.orderId = cart.orderId INNER JOIN item ON item.itemId = cart.itemId INNER JOIN customer ON customer.customerId = `order`.customerId GROUP BY cart.orderId")
        # SELECT ALL ITEMS IN THE SAME orderId
        carts = Cart.objects.raw("SELECT * FROM `cart` INNER JOIN `order` ON `order`.orderId = cart.orderId INNER JOIN item ON item.itemId = cart.itemId INNER JOIN customer ON customer.customerId = `order`.customerId")
        customers = Customer.objects.all()
        items = Item.objects.all()
        context = {
            'order_list' : orders,
            'cart_list' : carts,
            'customers' : customers,
            'STATUS_CHOICE' : Customer.CUSTOMER_STATUS_CHOICES,
            'items':items,
            'ITEM_TYPES':Item.ITEM_TYPE_CHOICES
        }
        return render(request, 'dashboard/index.html', context)

    def post(self, request):

        if 'addOrderBtn' in request.POST:
            customer_form = CustomerForm(request.POST)
            order_form = OrderForm(request.POST)
            cart_form = CartForm(request.POST)

            customer_obj = None
            print('START CUSTOMER BLOCK')
            if request.POST.get('customerId') == None:
            # CREATE CUSTOMER
                fname = request.POST.get('firstname')
                mname = request.POST.get('middlename')
                lname = request.POST.get('lastname')
                gender = request.POST.get('gender')
                status = request.POST.get('status')
                birthday = request.POST.get('birthday')
                contactNumber = request.POST.get('contactNumber')
                email = request.POST.get('email')

                customer_obj = Customer(firstname=fname, middlename=mname, lastname=lname, gender = gender, status = status, birthday=birthday, contactNumber= contactNumber, email=email)
                customer_obj.save()
                customerId = customer_obj.customerId
                print('Created Customer: [' +str(customerId) +'] '  +lname +', ' +fname)


            else:
                customerId = request.POST.get('customerId')
                print('CustomerId: [' +customerId +']')
                customer_obj = Customer.objects.get(customerId = customerId)

            print('START ORDER BLOCK')
            
            if request.POST.get('amount') != None:
            # CREATE ORDER
                amount = request.POST.get('amount')
                # orderDateTime = request.POST.get('orderDateTime') # NO NEED EVERYTIME WE CALL save() THE ORDER-RECORD WILL AUTO UPDATE/FILLED-IN

                # order_obj = Order(customerId=customerId, amount=amount, orderDateTime=orderDateTime)
                order_obj = Order(customerId=customer_obj, amount=amount)
                order_obj.save()
                print('[' +str(order_obj.customerId) +'] amount: ' +amount)

                print('START CART BLOCK')
            # CREATE CART
                numberOfItems = request.POST.get('numberOfItems')
                print('numberOfItems: ' +numberOfItems)
                numberOfItems = int(numberOfItems) # CONVERT FROM STRING TO INT

                itemIdList = request.POST.getlist('itemId[]')
                quantityList = request.POST.getlist('itemQuantity[]')
                
                index = 0
                while index < numberOfItems:
                    itemId = itemIdList[index]
                    quantity = quantityList[index]

                    cart_obj = Cart(orderId=order_obj, itemId=Item.objects.get(itemId = itemId), quantity=quantity)
                    cart_obj.save()

                    print("Created Item: [" +str(cart_obj.cartId) +'] ' +str(cart_obj.quantity) +'pcs')
                    index = index + 1

            else:
                print(order_form.errors)
                return HttpResponse('Invalid')
                
        elif 'deleteOrderBtn' in request.POST:
            orderId = request.POST.get('orderId')
            order_list = Order.objects.all()
            tartget = order_list.get(orderId = orderId)
            tartget.delete()
            print("deleted orderId: " +str(orderId))

        elif 'deleteOrderedItemBtn' in request.POST:
            cartId = request.POST.get('cartId')
            cart_list = Cart.objects.all()
            target = cart_list.get(cartId = cartId)

            orderId = target.orderId
            itemId = target.itemId.pk
            quantity = target.quantity
            target.delete()
            print("deleted cartId: " +str(cartId))

            checklist = Cart.objects.filter(orderId = orderId)
            print("len(checklist): " +str(len(checklist)))
            if len(checklist) < 1:
                Order.objects.get(orderId = orderId.pk).delete()
                print("deleted orderId: " +str(orderId))
            
            else:
                # target = Order.objects.filter(orderId = orderId.pk)
                # total_amount = target[0].amount
                # total_amount *= 100 # SCALE UP TO REMOVE 2 DECIMAL UNIT (NECESSARY FOR FLOAT PRECISION PROBLEM)
                
                # item = Item.objects.get(itemId = itemId)
                # item_price = item.price * 100 # SCALE UP TO REMOVE 2 DECIMAL UNIT (NECESSARY FOR FLOAT PRECISION PROBLEM)
                # total_amount = (total_amount - Decimal((quantity * item_price))) * Decimal(0.01) # SCALE DOWN TO RETURN TO 2 DECIMAL UNITS 
                
                # target.update(amount = total_amount)

                target = Order.objects.filter(orderId = orderId.pk)
                total_amount = target[0].amount
                
                item = Item.objects.get(itemId = itemId)
                item_price = item.price # NO NEED TO SCALE UP ( WHICH IS NECESSARY FOR FLOAT PRECISION PROBLEM) BECAUSE total_amount AND total_price IS DECIMAL-DATA-TYPE
                total_amount = total_amount - (quantity * item_price)
                
                target.update(amount = total_amount)
                
        return redirect('dashboard:index_view')

# OPTIONAL PWEDE RA IDELETE
class DashboardOrderView(View):
    def get(self, request):
        return render(request, 'dashboard/registration.html')
    

# REQUIRED
class DashboardCustomerView(View):
    def get(self, request):
        qs_customers = Customer.objects.all()
        context = {
            'customers' : qs_customers,
            'STATUS_CHOICE' : Customer.CUSTOMER_STATUS_CHOICES
        }
        # test = Customer.objects.get(customerId = 1)
        print(qs_customers[0].birthday)
        print('mewo')
        return render(request, 'dashboard/customer.html', context)

    def post(self, request):
        form = CustomerForm(request.POST)

        if 'addCustomer' in request.POST:

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

        elif 'updateButton' in request.POST:
            queryId = request.POST.get('customerId')
            
            fname = request.POST.get('fname')            
            mname = request.POST.get('mname')
            lname = request.POST.get('lname')
            gender = request.POST.get('gender')
            status = request.POST.get('status')
            birthday = request.POST.get('birthday')
            contactNumber = request.POST.get('contactNumber')
            email = request.POST.get('email')

            # QUERY ITEM WITH ID EQUAL TO queryId
            customer = Customer.objects.filter(customerId = queryId)
            print(customer[0].lastname)
            # UPDATE QUERRIED ITEM
            customer.update(firstname=fname, middlename=mname, lastname=lname, gender = gender, status = status, birthday=birthday, contactNumber= contactNumber, email=email)
            print("An Item has been updated!")        
            
        elif 'deleteButton' in request.POST:
            queryId = request.POST.get('customerId')
            # print(queryId)            
            # QUERY ITEM WITH ID EQUAL TO queryId
            customer = Customer.objects.filter(customerId = queryId)            
            customer.delete()
            print("An Item has been updated!")


        return redirect('dashboard:customer_view')
        
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
            print(queryId)
            # QUERY ITEM WITH ID EQUAL TO queryId
            item = Item.objects.filter(itemId = queryId)
            item.delete()
            print("An Item has been updated!")
            
        return redirect('dashboard:product_view') # EXECUTE DashboardProductView.get() METHOD self.get(request)

class CustomerIndexView(View):
    def get(self, request):
        qs_customers = Customer.objects.all()
        context = {
            'customers' : qs_customer
        }   
        return render(request, 'customer.html', context)