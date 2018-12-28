from django.shortcuts import render, redirect
from dalin.models import User
# Create your views here.



def haha(request):
    return redirect('/index/')


def index(request):
    if request.method == "GET":
        return render(request, 'User.html')
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        User.objects.create(username=username,password=password)
        print("我要插入了")
        return render(request,'success.html')