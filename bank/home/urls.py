from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('',views.index,name='index'),
    path('form/',views.form,name='form'),
    path('ajax/load_branch_details/', views.load_branch_details, name='load_branch_details'),
]