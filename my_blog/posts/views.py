from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import  View

# Create your views here.
class HelloWorld(View):
    def get(self, request):
        data = {
            'name': 'Diana Jardon',
            'years': 21,
            'codes': ['python', 'Django']
        }
        return render(request, 'hello_world.html', context=data)
