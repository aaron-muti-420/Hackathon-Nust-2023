from django.db import models

class RegisterUser(models.Model):

    DEPARTMENT_CHOICES = (
        ('department of computing and informatics','Department of Computing and Informatics'),
        ('department of journalism and communication','Department Of Journalism and Communication'),
        ('department of architecture','Department of Architecture'),
       
    )

    name_of_student = models.CharField(max_length=80)
    cell_phone = models.IntegerField()
    email_field = models.EmailField(max_length=255)
    faculty = models.CharField(max_length=100)

    department_graduated_from = models.CharField(max_length=255, choices=DEPARTMENT_CHOICES)
    home_address = models.CharField(max_length=150)
    motivation = models.TextField()


    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self) -> str:
        return self.name_of_student

