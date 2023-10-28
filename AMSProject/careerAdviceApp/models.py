from django.db import models

#Import the User from the authentication module in order to access system users
from django.contrib.auth.models import User
from django.db.models.query import QuerySet

#Implement the Tagging Manager
from taggit.managers import TaggableManager

#Import the timezone to determine the time of the user's system
from django.utils import timezone

#Objects is the default manager of every model that handles all CRUD Operations
"""
IT MAKES SENSE TO DEVELOP A SEPERATE MANAGER TO HANDLE ONLY THE PUBLISHED CALLS

1. YOU COULD ADD EXTRA MANAGER METHODS TO AN EXISTING MANAGER 
2. YOU COULD CREATE A NEW MANAGER BY MODIFYING THE INITIAL QUERYSET THAT THE MANAGER RETURNS

HENCE WE ARE USING OPTION 2

""" 


class PublishedCareerAdviceManager(models.Manager):
    def get_queryset(self):
        return super(PublishedCareerAdviceManager, self).get_queryset().filter(status='published')

class CareerAdvice(models.Model):
    # Use these choices to either show or hide each piece of advice
    STATUS_CHOICES = (
        ('draft','Draft'),
        ('published','Published'),
    )

    person_name = models.CharField(max_length=250)

    position = models.CharField(max_length=100)

    company = models.CharField(max_length=100)

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='career_advice')
   
    title_of_advice = models.CharField(max_length=100)
    
    the_advise = models.TextField()
    
    publish = models.DateTimeField(default=timezone.now)
    
    created = models.DateTimeField(auto_now_add=True)
    
    status = models.CharField(max_length=20, choices=STATUS_CHOICES,default='draft')

    # DEFAULT MODELS MANAGER
    objects = models.Manager()

    # OUR CUSTOM MODELS MANAGER
    publishedAdvice = PublishedCareerAdviceManager()
     
    #Instantiate the Manager
    tags = TaggableManager()
    """
            TAGS MANAGER ALLOWS
    1. Add
    2. Retrieve
    3. Remove Tags from Objects
    
    """
    
    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.person_name
    







