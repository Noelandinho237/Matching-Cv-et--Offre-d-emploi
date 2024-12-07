from django.db import models

# Create your models here.

class Offer(models.Model):
    id_offer = models.AutoField(primary_key=True,null=False)
    title_offer = models.CharField(max_length=255)
    description_offer = models.FileField(upload_to='Files/Offers')

    # New field for predicted category
    category = models.CharField(max_length=255, blank=True, null=True)  

    def __str__(self):
        return f"{self.title_offer}" 

class Cv(models.Model):
    id_cv = models.AutoField(primary_key=True,null=False)
    name = models.CharField(max_length=255,default='Unknown')
    description_cv = models.FileField(upload_to='Files/CVs')

    # New field for predicted category
    category = models.CharField(max_length=255, blank=True, null=True)  


    def __str__(self):
        return f"{self.id_cv}" 