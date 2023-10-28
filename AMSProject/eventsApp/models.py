from django.db import models


#OUR CUSTOM OBJECT MANAGER
class PublishedEventsManager(models.Manager):
    def get_queryset(self):
        return super(PublishedEventsManager, self).get_queryset().filter(status='published')

#Create Items to be tracked by Django
class EventsApp(models.Model):

    DEPARTMENT_CHOICES = (
        ('department of software development','Department Of software Development'),
        ('department of civil engineering','Department Of Civil Engineering'),
        ('department of tourism','Department Of Tourism'),
        ('inclusive','Inclusive')
    )

    STATUS_CHOICE = (
        ('draft','Draft'),
        ('pending','Pending'),
        ('published','Published'),
    )


    event_name = models.CharField(max_length=255)
    event_organizer = models.CharField(max_length=255)
    department = models.CharField(max_length=300,choices=DEPARTMENT_CHOICES)
    start_date = models.DateTimeField()
    end_date = models.DateField()
    status = models.CharField(max_length=50, choices=STATUS_CHOICE, default='draft')

    # Custom Header
    publishedEvents = PublishedEventsManager()

     #Create a meta class that contains the metadata for the model
    class Meta:
        #Sort the Articles by descending order, hence the negative prefix
        ordering = ('-start_date',)
    
    def __str__(self) -> str:
        return self.event_name