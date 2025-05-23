from django.db import models

# Create your models here.

STATUS_CHOICES = (
    ('sale', 'Sale'),
    ('sold', 'Sold'),
)

SUBURB_CHOICES = (
    ('silvermoonVillage', 'Silvermoon Village'),
    ('riverwood', 'Riverwood'),
    ('mystictown', 'Mystic Town'),
)

POSITION_CHOICES = (
    ('director', 'Director'),
    ('salesassociate', 'Sales Associate'),
    ('salesprofessional', 'Sales Professional'),
)

class Property(models.Model):
    address = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='sale')
    suburb = models.CharField(max_length=20, choices=SUBURB_CHOICES, default='silvermoonVillage')
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    image = models.ImageField(upload_to='properties/') #Our images will be stored in media/properties/
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.address

class Member(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    position = models.CharField(max_length=20, choices=POSITION_CHOICES, default='salesassociate')
    phone = models.CharField(max_length=15)
    image = models.ImageField(upload_to='members/') #Our images will be stored in media/members/


    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

class ContactInquiry(models.Model):

    SUBJECT_CHOICES = (
        ('selling', 'I\'m thinking of selling'),
        ('buying', 'I\'m thinking of buying'),
        ('career', 'Career Opportunities'),
        ('support', 'Customer Support'),
    )

    CONTACT_METHOD_CHOICES = (
        ('phone', 'Phone'),
        ('email', 'Email'),
    )    


    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=150)
    phone = models.CharField(max_length=15, blank=True, null=True) 
    subject = models.CharField(max_length=20, choices=SUBJECT_CHOICES)
    contact_method = models.CharField(max_length=10, choices=CONTACT_METHOD_CHOICES, default='email', blank=True, null=True) 
    message = models.TextField(max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Contact from {self.name}"

class SellRequest(models.Model):
    CONTACT_METHOD_CHOICES = (
        ('phone', 'Phone'),
        ('email', 'Email'),
    )        
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True, null=True) 
    property_address = models.CharField(max_length=255)
    contact_method = models.CharField(max_length=10, choices=CONTACT_METHOD_CHOICES, default='email', blank=True, null=True) 
    message = models.TextField(max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Sell request from {self.name}"