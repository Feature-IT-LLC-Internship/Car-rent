from django.shortcuts import render

def index(request):
    return render(request, 'frontend/index.html')
def signup(request):
    return render(request, 'frontend/signup.html')
# Create your views here.
def login(request):
    return render(request, 'frontend/login.html')
def updateprofile(request):
    return render(request, 'frontend/updateprofile.html')
def mycar(request):
    return render(request, 'frontend/mycar.html')
def bookings(request):
    return render(request, 'frontend/bookings.html')
def changepass(request):
    return render(request, 'frontend/changepass.html')
def addcar(request):
    return render(request, 'frontend/addcar.html')
def bookcar(request):
    return render(request, 'frontend/bookcar.html')
def rentcar(request):
    return render(request, 'frontend/rentcar.html')