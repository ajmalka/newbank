from django.contrib import messages
from django.http import HttpResponse
from django.views.generic import ListView,CreateView
from .models import Branch, District,Form,Account,Card
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
def index(request):
    obj = Branch.objects.all()
    obj1 = District.objects.all()

    return render(request,'index.html',{'obj':obj,'obj1':obj1})


def registerform(request):
    bran = Branch.objects.all()
    dist = District.objects.all()
    acc = Account.objects.all()
    cd = Card.objects.all()
    if request.method == 'POST':
        name = request.POST.get('Name')
        dob = request.POST.get('DOB')
        age = request.POST.get('Age')
        gender = request.POST.get('Gender')
        phone = request.POST.get('Phone')
        mail = request.POST.get('Email')
        address = request.POST.get('Address')
        district = request.POST.get('District')
        branch = request.POST.get('Branch')
        account = request.POST.get('Account')
        materials = request.POST.get('Materials')
        form = Form.objects.create(name=name, dob=dob, age=age, gender=gender, phone=phone, mail=mail, address=address, district=district, branch=branch, account=account, materials=materials)
        form.save()
        messages.info(request, "Application Accepted")
        print("applictaion accepted")

    return render(request, 'form.html', {'bran': bran, 'dist': dist, 'acc': acc, 'cd': cd})












