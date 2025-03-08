from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate, logout
from talentshield.forms import SignUpForm, LoginForm
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to TalentShield!")

def index(request):
   return render(request, 'index.html') 
# Ensure this matches the template name
def resume(request):
   return render(request, 'resumebuilder.html')

def upload(request):
   return render(request, 'upload.html')

def option(request):
   return render(request, 'option.html')

def signup(request):
    return render(request, 'signup.html')

def results(request):
   return render(request, 'results.html')

def profile(request):
   return render(request, 'profile.html')
def login(request):
    return render(request, 'login.html')

def candidate(request):
    return render(request, 'candidate.html')

def hrmanager(request):
    return render(request, 'hrmanager.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')  # Redirect to dashboard
    else:
        form = SignUpForm()
    return render(request, 'talentshield/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = LoginForm()
    return render(request, 'talentshield/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

   

   

