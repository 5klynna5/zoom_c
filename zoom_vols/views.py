from django.shortcuts import render, redirect, get_object_or_404
from .models import Volunteer, Hours, VolunteerGroup
from .forms import HoursForm, VolunteerForm, GroupHoursForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.db.models import Sum, Count
from collections import Counter

@login_required(login_url='/login/')
def volunteer_home(request):
    month = datetime.now().month
    year = datetime.now().year
    volunteer_hours_month = Hours.objects.filter(date__month=month).filter(date__year=year)
    total_vol_hours_month = volunteer_hours_month.aggregate(sum = Sum('hours_num'))
    total_vols_month = volunteer_hours_month.aggregate(count = Count('volunteer', distinct=True))
    group_hours_month = VolunteerGroup.objects.filter(date__month=month).filter(date__year=year)
    total_group_hours_month = 0
    for item in group_hours_month:
        total_group_hours_month = total_group_hours_month + item.total_group_hours
    group_vols_month = group_hours_month.aggregate(count = Sum('num_volunteers'))
    try:
        vols_combined = dict(Counter(total_vols_month) + Counter(group_vols_month))
    except TypeError:
        vols_combined = dict(Counter(total_vols_month))
    try:
        hours_combined = Counter(total_vol_hours_month) + Counter({'sum': total_group_hours_month})
    except TypeError:
        hours_combined = Counter({'sum' : total_group_hours_month})

    return render(request, 'zoom_vols/volunteer_home.html', {'month': month, 'year' : year, 'vols_combined' : vols_combined, 'hours_combined' : hours_combined, 'volunteer_hours_month': volunteer_hours_month, 'total_vol_hours_month': total_vol_hours_month, 'total_vols_month' : total_vols_month, 'group_hours_month': group_hours_month, 'group_vols_month' : group_vols_month, 'total_group_hours_month' : total_group_hours_month})

@login_required(login_url='/login/')
def volunteer_list(request):
	volunteers = Volunteer.objects.all()
	return render(request, 'zoom_vols/volunteer_list.html', {'volunteers' : volunteers})

@login_required(login_url='/login/')
def volunteer_group_list(request):
	groups = VolunteerGroup.objects.all().order_by('-date')
	return render(request, 'zoom_vols/volunteer_group_list.html', {'groups' : groups})

@login_required(login_url='/login/')
def volunteer_detail(request, pk):
    volunteer = get_object_or_404(Volunteer, pk=pk)
    return render(request, 'zoom_vols/volunteer_detail.html', {'volunteer': volunteer})

@login_required(login_url='/login/')
def hours_new(request):
    if request.method == "POST":
        form = HoursForm(request.POST)
        if form.is_valid():
            hours = form.save(commit=False)
            hours.save()
            return redirect('volunteer_home')
    else:
        form = HoursForm()
    return render(request, 'zoom_vols/hours_new.html', {'form': form})

@login_required(login_url='/login/')
def group_hours_new(request):
    if request.method == "POST":
        form = GroupHoursForm(request.POST)
        if form.is_valid():
            hours = form.save(commit=False)
            hours.save()
            return redirect('volunteer_home')
    else:
        form = GroupHoursForm()
    return render(request, 'zoom_vols/hours_new.html', {'form': form})

@login_required(login_url='/login/')
def volunteer_new(request):
    if request.method == "POST":
        form = VolunteerForm(request.POST)
        if form.is_valid():
            volunteer = form.save(commit=False)
            volunteer.save()
            return redirect('volunteer_list')
    else:
        form = VolunteerForm()
    return render(request, 'zoom_vols/volunteer_new.html', {'form': form})

@login_required(login_url='/login/')
def volunteer_edit(request, pk):
    volunteer = get_object_or_404(Volunteer, pk=pk)
    if request.method == "POST":
        form = VolunteerForm(request.POST, instance=post)
        if form.is_valid():
            volunteer = form.save(commit=False)
            post.save()
            return redirect('volunteer_detail', pk=volunteer.pk)
    else:
        form = VolunteerForm(instance=volunteer)
    return render(request, 'zoom_vols/volunteer_edit.html', {'form': form})
