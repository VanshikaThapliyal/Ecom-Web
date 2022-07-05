from django.contrib import admin
#importing the model from models.py
from home.models import Contact
# Register your models here.
admin.site.register(Contact)
#Contact.objects.all()[0].name in shell for query
#for filter=Contact.objects.filter(name="Vanshika Thapliyal",phone="07973379830")