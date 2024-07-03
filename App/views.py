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

    if request.method == "POST":
        print(1)
        from_city = request.POST['from']
        to_city = request.POST['to']
        departure = request.POST['departure']
        arrival = request.POST['arrival']
        flight_cls = request.POST['class']

        models.FindFlight.objects.create(
            departure = from_city,
            destination = to_city,
            departure_date = departure,
            arrival = arrival,
            class_type = flight_cls
        )
    return render(request, 'booking.html', context)

def mail(request):
    contact = models.ContactInfo.objects.last()
    context = {
        "contact" : contact
    }
    return render(request, 'mail.html', context)

def single(request):
    last = models.RecentVisitingPlaces.objects.last()
    last3 = models.RecentVisitingPlaces.objects.all().order_by('-id')[:3]
    places = models.RecentVisitingPlaces.objects.all()[:3]
    panel = models.CategoryPanel.objects.all()
    context = {
        "places" : places,
        "panel" : panel,
        "last" : last,
        "last3" : last3
    }
    return render(request, 'single.html', context)
