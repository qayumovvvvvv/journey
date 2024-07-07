from django.db import models


class RecentVisitingPlaces(models.Model):
    img = models.ImageField()
    title = models.CharField(max_length=255)
    body = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.title
    
    class Meta():
        verbose_name_plural = 'Places'


class AboutUs(models.Model):
    title = models.CharField(max_length=255)
    bodyH1 = models.TextField()
    body = models.TextField()

    def __str__(self):
        return self.title
    

    class Meta():
        verbose_name_plural = 'About Us'


class Our_team(models.Model):
    img = models.ImageField()
    name = models.CharField(max_length=255)
    body = models.TextField()

    def __str__(self):
        return self.name
    

    class Meta():
        verbose_name_plural = 'Our team'


class Provide(models.Model):
    img = models.ImageField()
    title = models.TextField()
    body = models.TextField()

    def __str__(self):
        return self.title
    

    class Meta():
        verbose_name_plural = 'Provide'


class HowToBook(models.Model):
    f_body = models.TextField()
    s_body = models.TextField()

    def __str__(self):
        return self.f_body
    
    class Meta():
        verbose_name_plural = 'How to Book'


class HowToBookStep(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()

    def __str__(self):
        return self.title
    
    class Meta():
        verbose_name_plural = 'Steps'


class FindFlight(models.Model):
    departure = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    departure_date = models.DateField()
    arrival = models.DateField()
    class_type = models.CharField(max_length=255)

    def __str__(self):
        return self.departure
    

    class Meta():
        verbose_name_plural = 'Find Flight'


class ContactInfo(models.Model):
    address = models.TextField()
    phone = models.CharField(max_length=20)
    fax = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.email
    

    class Meta():
        verbose_name_plural = 'Contact informations'

class Contact(models.Model):
    full_name = models.TextField()
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.email
    

    class Meta():
        verbose_name_plural = 'Contacts'


class SignUp(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email
    
    class Meta():
        verbose_name_plural = 'Sing ups'


class Reply(models.Model):
    message = models.TextField()


    class Meta():
        verbose_name_plural = 'Replies'



class CategoryPanel(models.Model):
    category = models.TextField()

    def __str__(self):
        return self.category
    
    class Meta():
        verbose_name_plural = 'Categories'