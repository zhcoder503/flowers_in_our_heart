from django.shortcuts import render
from .models import Profile

def index(request):
    profile_list=Profile.objects.all()


    return render(request,'index.html',{'profile_list':profile_list})

