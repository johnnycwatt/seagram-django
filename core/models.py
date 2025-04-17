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
    