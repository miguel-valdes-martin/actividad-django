from django.shortcuts import render, HttpResponse
from . import models
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import DestinationForm

def index(request):
    return render(request, 'index.html')

def about(request): 
    return render(request, 'about.html')

def destinations(request):
    all_destinations = models.Destination.objects.all()
    return render(request, 'destinations.html', {'destinations': all_destinations})

class DestinationCreate(CreateView):
    model = models.Destination
    form_class = DestinationForm
    template_name = "destination_form.html"
    success_url = reverse_lazy("destinations")
