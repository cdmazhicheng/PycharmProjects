from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def first_login(request):
    error_msg = "error_login"
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        if username == "mazhicheng" and password == "123456":
            return HttpResponse(request.get_host())
        else:
            return HttpResponse(error_msg)
    return render(request, 'login.html')
