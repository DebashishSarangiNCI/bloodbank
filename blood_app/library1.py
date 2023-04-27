from django.shortcuts import render
from .models import UserProfile, Blood_Donation, Order


def history_view(request):
    user = UserProfile.objects.get(user=request.user)
    data = Blood_Donation.objects.filter(user=user)
    return render(request, "history.html", {'data':data})
    
def myorder(request):
    user = UserProfile.objects.get(user=request.user)
    data = Order.objects.filter(user=user)
    return render(request, "my_order.html",{'data':data})

def allorder(request):
    data = Order.objects.filter()
    return render(request, "all_order.html",{'data':data})
    
def viewuser(request):
    data = UserProfile.objects.all()
    d = {'data':data}
    return render(request,'view_user.html',d)