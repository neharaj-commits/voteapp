from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import User,Candidates
from django.template import loader
from django.shortcuts import get_object_or_404,render
from django.http import Http404
from django.urls import reverse
from django.views import generic
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import NewUserForm
def index(request):
    return render (request= request,
                   template_name = "polls/index.html",
                   context = {"use": User.objects.all})
    
# Create your views here.
def signup(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"New Account Created:{username}")
            login(request, user)
            messages.info(request, f"You are now logged in as {username}")
            return redirect("polls:index")
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg} : form.error_messages[msg]")
                # print(form.error_messages[msg])

    form = NewUserForm
    return render(request, 
                  "polls/signup.html",
                  context = {"form":form} )

def logout_request(request):
    logout(request)
    messages.info(request,"Logged out successfully")
    return redirect("polls:index")

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate (username = username,password = password)
            if user is not None :
                login(request,user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect("polls:index")
            else:
                messages.error(request,"Invalid username or password")

        else:
            messages.error(request,"Invalid username or password")
    
    
    form = AuthenticationForm()
    return render(request,
                   "polls/login.html",
                   {"form" : form})



def vote(request):

    if request.method == 'POST':
        if request.POST["choice"]:
            selected_choice = Candidates.objects.get(pk=request.POST['choice'])
            selected_choice.votes += 1
            selected_choice.save()
            messages.info(request, f"You voted for {selected_choice.cand_name}")
            return redirect('polls:index')
        else:
            return render(request, 'polls/vote.html', {'error_message': "Please select a choice "})
    return render(request, 'polls/vote.html' , {'Candlist': Candidates.objects.all()})
