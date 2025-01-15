from django.db import models

class Contact(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

 


class Book(models.Model):
    fullName = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.TextField()
    dob = models.DateField()
    passport = models.TextField()
    destination = models.CharField(max_length=100)
    hotel = models.CharField(max_length=100)
    startDate = models.TextField()
    endDate = models.TextField()
    adults = models.CharField(max_length=100)
    children = models.CharField(max_length=100)
    typeTrip = models.CharField(max_length=100)
    specialRequests = models.TextField()
    roomType = models.CharField(max_length=100)
    add_services = models.CharField(max_length=100, choices=[('yes', 'Travel Insurance'), ('yes', 'Air Pickup'), ('yes', 'Guided Tours')])
    customExperience = models.CharField(max_length=100)
    paymentMethod = models.CharField(max_length=100, choices=[('credit', 'Credit/Debit Card'), ('paypal', 'PayPal')])
    cardName = models.CharField(max_length=100)
    expiry = models.CharField(max_length=100)
    cvv = models.CharField(max_length=100)
    billingAddress = models.CharField(max_length=100)
        

   