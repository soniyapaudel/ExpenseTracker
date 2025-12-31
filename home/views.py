from django.shortcuts import render,redirect
from django.contrib.auth import login as dj_login
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth import logout
from .models import Addmoney_info
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import UserProfile

def index(request):
    return render(request, 'home/index.html')

def login_page(request):
    return render(request,'home/login.html')

def register(request):
    return render(request, 'home/register.html' )

def handleSignup(request):
    if request.method =='POST':
        # Get form data 

        name= request.POST['name']
        email =request.POST['email']
        phone =request.POST['phone']
        password1 =request.POST['pass1']
        password2 =request.POST['pass2']

        # validation 
        if password1 != password2:
            messages.error(request, "Passwords do not match!")
            return redirect('register')
        

        if User.objects.filter(username=name).exists():
            messages.error(request, "Username already exists!")
            return redirect('register')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered!")
            return redirect('register')
        if len(password1) <6:
            messages.error(request, "Password must be at least 6 characters!")
            return redirect('register')


        # create User
        user = User.objects.create_user(
            username = name,
            email= email,
            password=password1
        )    
        user.save()    

        #create User profile

        user_profile = UserProfile.objects.create(
            user=user,
            savings =0,
            income=0
        )
        user_profile.save()

        messages.success(request, "Account created successfully! Please Login.")
        return redirect('login')
    
    return redirect('register')



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
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid credentials, please try again")
            return redirect("login")
    return redirect('login')


@login_required(login_url='login')
def dashboard(request):
    user = request.user

        # get user profile or create if doesn't exists

    user_profile, created = UserProfile.objects.get_or_create(
            user = user,
            defaults= {'savings': 0, 'income':0}
        )


            # get all transactions for this user only 

    user_expenses = Addmoney_info.objects.filter(user=user)


    # calculate totals

    total_income = sum(exp.amount for exp in user_expenses if exp.add_money == 'Income')
    total_expense = sum(exp.amount for exp in user_expenses if exp.add_money == 'Expense')
    balance = total_income - total_expense


    context={
        'user_expenses': user_expenses,
        'username': user.username,
        'user_profile': user_profile,
        'total_income': total_income,
        'total_expense': total_expense,
        'balance': balance,
    }

    return render(request, 'home/dashboard.html', context)
        
@login_required(login_url ='login')
def handlelogout(request):
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect('login')