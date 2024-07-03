from django.shortcuts import render
from . import models

def main(request):
    places = models.RecentVisitingPlaces.objects.all()
    context = {
        "places" : places
    }
    return render(request, 'index.html', context)

def about(request):
    about = models.AboutUs.objects.last()
    team = models.Our_team.objects.all()
    context = {
        "about" : about,
        "teams" : team
    }
    return render(request, 'about.html', context)

def booking(request):
    provide = models.Provide.objects.last()
    book = models.HowToBook.objects.last()
    steps = models.HowToBookStep.objects.all()
    places = models.RecentVisitingPlaces.objects.all()
    context = {
        "provide" : provide,
        "book" : book, 
        "steps" : steps, 
        "places" : places, 
    }
    return render(request, 'booking.html', context)

def mail(request):
    contact = models.ContactInfo.objects.last()
    context = {
        "contact" : contact
    }
    return render(request, 'mail.html', context)

def single(request):
    places = models.RecentVisitingPlaces.objects.all()
    panel = models.CategoryPanel.objects.all()
    context = {
        "places" : places,
        "panel" : panel
    }
    return render(request, 'single.html', context)
