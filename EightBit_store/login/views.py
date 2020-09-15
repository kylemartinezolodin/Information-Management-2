from django.shortcuts import render
from django.views.generic import View

# Create your views here.
class LoginIndexView(View):
    def get(self, request):
        return render(request, 'login/index.html')