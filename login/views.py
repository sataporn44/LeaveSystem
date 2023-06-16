from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from login.models import Person
from .models import Person


# Create your views here.

def index(request):
    return render(request, 'index.html')

def createForm(request):
    return render(request, 'createForm.html')

def info(request):
    try:
        person=Person.objects.get(username=request.username)
    except Exception as e:
        person = None
        print('Exception : ', e)

    context = {
        'person': person,
    }

    return render(request, 'info.html')

def addForm(request):
    if request.method == "POST":
        username=request.POST.get('username')
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        nickname=request.POST.get('nickname')
        tel=request.POST.get('tel')
        team=request.POST.get('team')
        position=request.POST.get('position')
        email=request.POST.get('email')
        password=request.POST.get('password')
        leader=request.POST.get('leader')

        person=Person.objects.create(
            username=username,
            first_name=first_name,
            last_name=last_name,
            nickname=nickname,
            tel=tel,
            team=team,
            position=position,
            email=email,
            password=password,
            leader=leader
        )
        person.set_password(password)  #แปลงpasswordเป็นการเข้ารหัส
        person.save()
        return render(request, "result.html")

    else:
        return render(request, "createForm.html")

def login(request):
        username=request.POST.get('username')
        password=request.POST.get('password')
        #try:
         #   user = Person.objects.get(username=username , password=password)
        #except:
         #   user = None
    

        user=auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            if user.position=='HR':
               return redirect('/hr')
            elif user.position=='Boss':
               return redirect('/leader')
            else:
                return redirect('/info')
        else:
            messages.info(request, 'Username or Password is incorrect')
            return redirect('/')

def hr(request):
    return render(request, 'hr.html')

def leader(request):
    return render(request, 'leader.html')

   

    

    


    

    
    
    







