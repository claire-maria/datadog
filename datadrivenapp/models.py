from django.db import models
from django.forms import ModelForm

# Create your models here.
class Pet(models.Model):
    pet_name = models.CharField(max_length = 100)
    pet_age = models.CharField(max_length = 2)
    pet_img = models.ImageField(upload_to ='uploads/') 
    pet_paragraph = models.CharField(max_length = 1000)
    date_entered = models.DateTimeField()

    def __str__(self):
        return self.pet_name + " " + self.pet_age


class PetForm(ModelForm):
    class Meta:
        model = Pet
        fields = '__all__'