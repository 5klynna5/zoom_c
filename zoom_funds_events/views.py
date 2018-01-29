from django.shortcuts import render, get_object_or_404, redirect
from .models import Event, Grant
from .forms import EventForm, GrantForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def events_list(request):
    events = Event.objects.all()
    return render(request, 'zoom_funds_events/events_list.html', {'events': events})

@login_required(login_url='/login/')
def event_new(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.save()
            return redirect('events_list')
    else:
        form = EventForm()
    return render(request, 'zoom_funds_events/event_new.html', {'form': form})

@login_required(login_url='/login/')
def grants_list(request):
    grants = Grant.objects.all().order_by('-grant_end_date')
    return render(request, 'zoom_funds_events/grants_list.html', {'grants': grants})

@login_required(login_url='/login/')
def grant_new(request):
    if request.method == "POST":
        form = GrantForm(request.POST)
        if form.is_valid():
            grant = form.save(commit=False)
            grant.save()
            return redirect('grants_list')
    else:
        form = GrantForm()
    return render(request, 'zoom_funds_events/grant_new.html', {'form': form})