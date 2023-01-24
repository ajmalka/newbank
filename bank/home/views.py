from django.contrib import messages
from django.utils.safestring import mark_safe

from .forms import BookingForm
from .models import District
from django.shortcuts import render

from .models import  Branch
def index(request):
    obj = Branch.objects.all()
    obj1 = District.objects.all()

    return render(request,'index.html',{'obj':obj,'obj1':obj1})


def form(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request,mark_safe("Application accepted <a href='/'> &ensp; &ensp; &ensp; &ensp; &ensp; &ensp;Go back home</a>"))

    form = BookingForm()
    dict_form = {
        'form': form
    }
    return render(request,'form.html',dict_form)


def load_branch_details(request):
    district_id = request.GET.get('district_id')
    branches = Branch.objects.filter(
        district=district_id).order_by('name')
    return render(request, 'load_branch_dropdown_list.html', {'branches': branches})
