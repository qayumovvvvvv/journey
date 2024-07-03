from django.shortcuts import render

def main(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def mail(request):
    return render(request, 'mail.html')

def booking(request):
    return render(request, 'booking.html')

def single(request):
    return render(request, 'single.html')

def ind(request):
    return render(request, 'ind.html')