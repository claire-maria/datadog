from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Pet, PetForm
# Create your views here.
def index(request):
    all_pets = Pet.objects.all()
    context = {
        'pet_list': all_pets,
    }
    return render(request, "index.html", context)
    

def edit_pets(request, pet_id = None):
    if(request.method == "POST"):
        if(pet_id is not None):
            pet = Pet.objects.get(id=pet_id)
            form = PetForm(request.POST,  request.FILES, instance = pet)

        else:
            form = PetForm(request.POST, request.FILES)
        if(form.is_valid()):
            form.save()
            return redirect(index)
    else:
        if(pet_id is not None):
            pet = Pet.objects.get(id=pet_id)
            form = PetForm(request.POST,  request.FILES, instance = pet)
        else:
            form = PetForm()
  
    return render(request, "form.html", {'form': form, 'pet_id': pet_id})

def del_pet(request, pet_id = None):
    pet = Pet.objects.get(id=pet_id)
    pet.delete()
    return redirect(index)