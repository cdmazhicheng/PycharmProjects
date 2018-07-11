from django.shortcuts import render
from .models import SoccerSite

# Create your views here.

def display(request):
    #sqltest内容
    testbegin = "准备完成......"
    soccersite_list = SoccerSite.objects.count()
    context= {

        'testbegin':testbegin,
        'soccersite_list': soccersite_list,
    }

    return render(request,'displayweb.html',context)
