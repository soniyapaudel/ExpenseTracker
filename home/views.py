from django.shortcuts import render,redirect
from django.contrib.auth import login as dj_login
from django.contrib.auth import authenticate
from django.contrib import messages
# Create your views here.
def home(request):
    if request.session.has_key('is_logged'):
        return redirect('/index')
    return render(request, 'home/login.html')

def index(request):
    if request.session.has_key('is_logged'):
        return render(request, 'home/index.html')
    return redirect('home')


def handlelogin(request):
    if request.method == 'POST':
        login_user_name = request.POST["login_user_name"]
        loginpassword1 = request.POST["loginpassword1"]

        user = authenticate(username=login_user_name, password=loginpassword1)

        if user is not None:
            dj_login(request, user)
            request.session['is_logged'] = True
            request.session['user_id'] = user.id
            messages.success(request, "Successfully logged in")
            return redirect('/index')
        else:
            messages.error(request, "Invalid credentials, please try again")
            return redirect("/")
    return redirect('/')

