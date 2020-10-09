from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required
from .models import Profile
from chat.models import User,Rooms,Participants



# Create your views here.
def home(request):
    username = None
    members = None
    grp = None
    if request.user.is_authenticated:
        user_id = request.user.id
        members = User.objects.get(id = user_id)
        # grp = Participants.objects.get(user = members)
        # # grp = Rooms.objects.all()
        for i in members.rooms_set.all():
            print(i.title)
        print(f' user id = {members.first_name}')
        # print(f' participant id = {grp.user.first_name}')
    return render(request,'home.html',{'member':members, 'grp':grp})    

def register(request):
    if request.method == "POST":
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        user_name = request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        print(request.POST)
        if password1 == password2:
            if not User.objects.filter(email=email).exists():
                if not User.objects.filter(username=user_name).exists():
                    user = User.objects.create_user(username=user_name,email=email,password=password1,first_name=first_name,last_name=last_name)
                    user.save()
                    print('user created')
                    return redirect('home')
                else:
                    print('username taken')
                    return redirect('register')
            else:
                print('email taken')
                return redirect('register')

        else:
            print('password not matching')
            return redirect('register')

    else:
        return render(request,'register.html')

def user_login(request):
    if request.method =="POST":
        username=request.POST['username']
        password=request.POST['password']

        user = auth.authenticate(request,username = username, password = password)
        if user:
            auth.login(request,user=user)
            if request.GET.get('next', None):
                return redirect(request.GET["next"])
            return redirect('home')
        else:
            return render(request,'login.html',{'error':'Please provide correct credintials'})
    else:
        return render(request,'login.html')
        
@login_required(login_url = 'user_login')
def user_logout(request):
    auth.logout(request)
    return redirect('home')
