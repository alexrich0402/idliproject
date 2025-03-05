from django.shortcuts import render

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


   

   

