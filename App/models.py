from django.db import models


class RecentVisitingPlaces(models.Model):
    img = models.ImageField()
    title = models.CharField(max_length=255)
    body = models.TextField()
    date = models.DateField()


class AboutUs(models.Model):
    title = models.CharField(max_length=255)
    bodyH1 = models.TextField()
    body = models.TextField()


class Our_team(models.Model):
    img = models.ImageField()
    name = models.CharField(max_length=255)
    body = models.TextField()


class Provide(models.Model):
    img = models.ImageField()
    title = models.TextField()
    body = models.TextField()


class HowToBook(models.Model):
    f_body = models.TextField()
    s_body = models.TextField()


class HowToBookStep(models.Model):
    number = models.IntegerField()
    title = models.CharField(max_length=255)
    body = models.TextField()

class FindFlight(models.Model):
    departure = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    departure_date = models.DateField()
    arrival = models.DateField()
    class_type = models.CharField(max_length=255)


class ContactInfo(models.Model):
    address = models.TextField()
    phone = models.CharField(max_length=20)
    fax = models.CharField(max_length=20)
    email = models.EmailField()


class Contact(models.Model):
    full_name = models.TextField()
    email = models.EmailField()
    message = models.TextField()


class SignUp(models.Model):
    email = models.EmailField()


class Reply(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()


class Category():
    name = models.CharField(max_length=255)
