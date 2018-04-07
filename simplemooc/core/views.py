from django.shortcuts import render
from django.http import HttpResponse

<<<<<<< HEAD
def home(request):
    return render(request, 'home.html')

def contact(request):
    return render(request, 'contact.html')
=======
# Create your views here.
def home(request):
	return render (request, 'home.html',{'usuario' : 'Gabriel Vieira'})

def contact (request):
	return render(request, 'contact.html')
>>>>>>> 46ce90fe4035ea380c6e6b06ca8d29d0aacfcef6
