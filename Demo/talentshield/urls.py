from django.urls import path
from .views import index, resume, upload, option, signup, results, profile, login, candidate, hrmanager, dashboard

urlpatterns = [
    path('', index, name='talentShield'),
    path('resumebuilder.html', resume, name='resumepage'),
    path('upload.html', upload, name='uploadpage'),
    path('option.html', option, name='optionpage'),
    path('signup.html', signup, name='signuppage'),
    path('results.html', results, name='resultpage'),
    path('profile.html', profile, name='profilepage'),
    path('login.html', login, name='loginpage'),
    path('candidate.html', candidate, name='candidatepage'),
    path('hrmanager.html', hrmanager, name='hrmanagerpage'),
    path('dashboard.html', dashboard, name='dashboardpage'),
]
