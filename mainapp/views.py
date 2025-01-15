from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Contact
# Create your views here.
def home(request):
    return render(request, "index.html")
def about(request):
    return render(request, "about.html")
def contact(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        contact = Contact(full_name=full_name,email=email, message=message)
        contact.save()

        return redirect('home')

    return render(request, 'contact.html')

def services(request):
    return render(request, "services.html")
def book(request):
    return render(request, "book.html")
def info(request):
    return render(request, "info.html")
def news(request):
    return render(request, "news.html")    
def flight(request):
    return render(request, "flight.html")
def hotels(request):
    return render(request, "hotels.html")
def trip(request):
    return render(request, "trip.html")
def cars(request):
    return render(request, "cars.html")
def activities(request):
    return render(request, "activities.html")



