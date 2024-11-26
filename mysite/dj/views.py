from django.shortcuts import render,HttpResponse
from dj.models import contact,Team

# Create your views here.

def index(request):
    obj=Team.objects.all()
    members={}
    for i,single in zip(range(len(obj)),obj):
        members['img'+str(i)]=obj[i].img
        members['name'+str(i)]=obj[i].name
        members['position'+str(i)]=obj[i].position
        members['discription'+str(i)]=obj[i].discription
    
    return render(request,'index.html',members)


def contactData(request):
    name=request.POST['name']
    email=request.POST['email']
    subject=request.POST['subject']
    message=request.POST['message']

    obj=contact(name=name,email=email,subject=subject,message=message)
    obj.save()
    msg="Data is Saved Succecfuly"
    return HttpResponse({msg:'mag'})


