from django.shortcuts import render
from .models import UserProfile, Blood_Donation, Order

# view for displaying the blood donation history of a user
def history_view(request):
    # get the UserProfile instance of the current user
    user = UserProfile.objects.get(user=request.user)
    # get all Blood_Donation instances associated with the user
    data = Blood_Donation.objects.filter(user=user)
    # render the history.html template with the Blood_Donation instances as context data
    return render(request, "history.html", {'data':data})
    
# view for displaying the order history of a user
def myorder(request):
    # get the UserProfile instance of the current user
    user = UserProfile.objects.get(user=request.user)
    # get all Order instances associated with the user
    data = Order.objects.filter(user=user)
    # render the my_order.html template with the Order instances as context data
    return render(request, "my_order.html",{'data':data})

# view for displaying all orders
def allorder(request):
    # get all Order instances
    data = Order.objects.filter()
    # render the all_order.html template with the Order instances as context data
    return render(request, "all_order.html",{'data':data})
    
# view for displaying all users
def viewuser(request):
    # get all UserProfile instances
    data = UserProfile.objects.all()
    # create a dictionary with the UserProfile instances as value for the 'data' key
    d = {'data':data}
    # render the view_user.html template with the dictionary as context data
    return render(request,'view_user.html',d)
