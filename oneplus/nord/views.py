from django.shortcuts import render
from .models import *

# Create your views here.
def form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        data = User(name=name, email=email, phone=phone)
        data.save()
    template = 'nord/form.html'
    return render(request,template)


def data(request):
    template = 'nord/data.html'
    obj = User.objects.all()
    return render(request, template, context={'obj':obj})