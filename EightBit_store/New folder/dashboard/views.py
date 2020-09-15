from django.shortcuts import render
from django.views.generic import View

# Create your views here.
class DashboardIndexView(View):
    def get(self, request):
        return render(request, 'dashboard/index.html')

class DashboardOrderView(View):
    def get(self, request):
        return render(request, 'dashboard/registration.html')