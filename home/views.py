from django.shortcuts import render,redirect
from django.contrib.auth import login as dj_login
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth import logout
from .models import Addmoney_info
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'home/index.html')

def login_page(request):
    return render(request,'home/login.html')

def register(request):
    return render(request, 'home/register.html' )
# def handlelogin(request):
#     if request.method == 'POST':
#         login_user_name = request.POST["login_user_name"]
#         loginpassword1 = request.POST["loginpassword1"]

#         user = authenticate(username=login_user_name, password=loginpassword1)

#         if user is not None:
#             dj_login(request, user)
#             request.session['is_logged'] = True
#             request.session['user_id'] = user.id
#             messages.success(request, "Successfully logged in")
#             return redirect('/index')
#         else:
#             messages.error(request, "Invalid credentials, please try again")
#             return redirect("/")
#     return redirect('/')

# def handleLogout(request):
#     del request.session['is_logged']
#     del request.session['user_id']
#     logout(request)
#     messages.success(request, "Successfully logged out")
#     return redirect('home')


# def register(request):
#     return render(request, 'home/register.html')


# def addexpense(request):
#     return render(request, 'home/addexpense.html')


# @login_required(login_url='/login/')
# def handleExpenses(request):
#     if request.method == 'POST':
#         amount = request.POST.get('amount')
#         description = request.POST.get('description')
#         category = request.POST.get('category')
#         date = request.POST.get('date')

#         # Create and Save Expenses
#         Addmoney_info.objects.create(
#             user=request.user,
#             add_money='Expense',
#             amount = amount,
#             description = description,
#             category = category,
#             date = date

#         )
        

#         messages.success(request, 'Expense added successfully!')
#         return redirect('/addexpense')

#     return redirect('/addexpense/')
