from django.db import models

# Create your models here.

#Custom Manager
class PublishedGalleryManager(models.Manager):
    def get_queryset(self):
        return super(PublishedGalleryManager, self).get_queryset().filter(status='published')


class AlumniGallery(models.Model):

    STATUS_CHOICES = (
        ('draft','Draft'),
        ('published','Published')
    )

    name_of_event = models.CharField(max_length=255)
    date_of_event = models.DateTimeField()
    event_location = models.CharField(max_length=250,default="Unknown")
    extra_info = models.TextField()
    status = models.CharField(max_length=12,choices=STATUS_CHOICES, default='draft')
    #Add a field for the image
    event_image = models.ImageField(upload_to="images/")

    publishedGallery = PublishedGalleryManager()

    class Meta:
        #Sort the Articles by descending order, hence the negative prefix
        ordering = ('-date_of_event',)


    def __str__(self) -> str:
        return self.name_of_event




