from django.shortcuts import render
from hobby.models import Mentor
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect 
from django.db.models import Q

def index(request):
    MyMentor = Mentor.objects.all().values()
    context = {
        'nickname':'Hamdan',
        'MyMentor':MyMentor,
    }
    return render(request, "index.html", context)

def NewMentor(request):
    displaydata = Mentor.objects.all().values()
    if request.method == 'POST':
        menid1 = request.POST['mentorid']
        menname1 = request.POST['mentorname']
        menroomno1 = request.POST['roomno']
        data = Mentor(MentorID = menid1, MentorName = menname1, RoomNo = menroomno1)
        data.save()

        context = {
            'displaydata':displaydata,
            'message':'NEW MENTOR HAS BEEN ADDED',
        }
        
        return render(request, "NewMentor.html", context)   
    else:
        dict = {
            'message':'',
            'displaydata':displaydata,
        }
    return render(request, "NewMentor.html", dict)   

def update(request, MentorID):
    updateid = Mentor.objects.get(MentorID = MentorID)
    dict = {
        'updateid':updateid
    }
    return render(request, "update.html", dict)

def updatedata(request, MentorID):
    data = Mentor.objects.get(MentorID = MentorID)
    menname = request.POST['mentorname']
    menroomno = request.POST['roomno']
    data.MentorName = menname
    data.RoomNo = menroomno
    data.save()

    return HttpResponseRedirect(reverse("newmentor"))

def viewdelete(request, MentorID):
    datanakdelete = Mentor.objects.get(MentorID = MentorID)
    dict = {
        'datanakdelete':datanakdelete
    }
    return render(request, "delete.html",dict)
    
def delete(request, MentorID):
    deletementor = Mentor.objects.get(MentorID = MentorID)
    deletementor.delete()
    
    return HttpResponseRedirect(reverse("newmentor"))

def searchpage(request):
    findmentor = Mentor.objects.filter(Q(MentorID = request.GET.get('Search')))
    dict = {
        'findmentor':findmentor
    }
    return render(request, 'searchpage.html',dict)