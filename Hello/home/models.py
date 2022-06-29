from django.db import models
#make migrations-create changes and store in a file
#migrations-apply the pending changes by makemigrations
#CONTAINS THE INFORMATION FOR MAKING THE DATABASE 

# Create your models here.
#creating a contact class
#this all is to be shown in the database
class Contact(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    phone=models.CharField(max_length=12)
    desc=models.TextField()
    date=models.DateField()
    def __str__(self):
         return self.name