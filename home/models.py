from django.db import models

# Create your models here.
class Ourstory(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.IntegerField()
    address = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name +"  "+ self.email
    