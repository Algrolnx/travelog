from django.shortcuts import render, get_object_or_404
from .models import Trip

def trip_list(request):
    trips = Trip.objects.all()
    return render(request, 'travelog/trip_list.html', {'trips': trips})

def trip_detail(request, pk):
    trip = get_object_or_404(Trip, pk=pk)
    return render(request, 'travelog/trip_detail.html', {'trip': trip})
