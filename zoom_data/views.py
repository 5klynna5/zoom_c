from django.shortcuts import render, get_object_or_404, redirect
from .models import Resident, Goal, Progress, Household, Child, Activity
from .forms import GoalForm, ResidentForm, ProgressForm, HouseholdForm, ChildForm, PermissionsForm, ActivityForm, AttendanceForm, ChildAttendanceForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.utils.timezone import datetime

@login_required(login_url='/login/')
def home(request):
    ##make a json from the database to use in d3 viz
    return render(request,'zoom_data/home.html')

@login_required(login_url='/login/')
def activities_list(request):
	activities = Activity.objects.all()
	return render(request, 'zoom_data/activities_list.html', {'activities' : activities})

@login_required(login_url='/login/')
def activity_detail(request, pk):
    activity = get_object_or_404(Activity, pk=pk)
    return render(request, 'zoom_data/activity_detail.html', {'activity': activity})

@login_required(login_url='/login/')
def resident_list(request):
	residents = Resident.objects.filter(resident_exit__isnull = True).order_by('resident_last_name')
	return render(request, 'zoom_data/resident_list.html', {'residents' : residents})

@login_required(login_url='/login/')
def resident_detail(request, pk):
    resident = get_object_or_404(Resident, pk=pk)
    return render(request, 'zoom_data/resident_detail.html', {'resident': resident})

@login_required(login_url='/login/')
def goal_detail(request, pk):
    goal = get_object_or_404(Goal, pk=pk)
    return render(request, 'zoom_data/goal_detail.html', {'goal': goal})

@login_required(login_url='/login/')
def child_detail(request, pk):
    child = get_object_or_404(Child, pk=pk)
    return render(request, 'zoom_data/child_detail.html', {'child': child})

@login_required(login_url='/login/')
def goal_new(request, pk):
    resident = get_object_or_404(Resident, pk=pk)
    if request.method == "POST":
        form = GoalForm(request.POST)
        if form.is_valid():
            goal = form.save(commit=False)
            goal.goal_resident = resident
            goal.save()
            return redirect('resident_detail', pk = resident.pk)
    else:
        form = GoalForm()
    return render(request, 'zoom_data/goal_new.html', {'form': form})

@login_required(login_url='/login/')
def household_new(request):
    if request.method == "POST":
        form = HouseholdForm(request.POST)
        if form.is_valid():
            household = form.save(commit=False)
            household.save()
            return redirect('household_list')
    else:
        form = HouseholdForm()
    return render(request, 'zoom_data/household_new.html', {'form': form})

@login_required(login_url='/login/')
def activity_new(request):
    if request.method == "POST":
        form = ActivityForm(request.POST)
        if form.is_valid():
            activity = form.save(commit=False)
            activity.save()
            return redirect('activities_list')
    else:
        form = ActivityForm()
    return render(request, 'zoom_data/activity_new.html', {'form': form})

@login_required(login_url='/login/')
def attendance_new(request, pk):
    activity = get_object_or_404(Activity, pk=pk)
    if request.method == "POST":
        form = AttendanceForm(request.POST)
        if form.is_valid():
            attendance = form.save(commit=False)
            attendance.activity = activity
            attendance.save()
            return redirect('activity_detail', pk = activity.pk)
    else:
        form = AttendanceForm()
        args = {}
        args['form'] = form
    return render(request, 'zoom_data/attendance_new.html', {'form': form, 'activity': activity})

@login_required(login_url='/login/')
def child_attendance_new(request, pk):
    activity = get_object_or_404(Activity, pk=pk)
    if request.method == "POST":
        form = ChildAttendanceForm(request.POST)
        if form.is_valid():
            childattendance = form.save(commit=False)
            childattendance.activity = activity
            childattendance.save()
            return redirect('activity_detail', pk = activity.pk)
    else:
        form = ChildAttendanceForm()
        args = {}
        args['form'] = form
    return render(request, 'zoom_data/attendance_new.html', {'form': form, 'activity': activity})

@login_required(login_url='/login/')
def add_progress(request, pk):
    goal = get_object_or_404(Goal, pk=pk)
    if request.method == "POST":
        form = ProgressForm(request.POST)
        if form.is_valid():
            progress = form.save(commit=False)
            progress.goal = goal
            progress.save()
            return redirect('goal_detail', pk = goal.pk)
    else:
        form = ProgressForm()
        args = {}
        args['form'] = form
    return render(request, 'zoom_data/add_progress.html', {'form': form})


@login_required(login_url='/login/')
def resident_new(request, pk):
    household = get_object_or_404(Household, pk=pk)
    if request.method == "POST":
        form = ResidentForm(request.POST)
        if form.is_valid():
            resident = form.save(commit=False)
            resident.household = household
            resident.save()
            return redirect('household_list')
    else:
        form = ResidentForm()
        args = {}
        args['form'] = form
    return render(request, 'zoom_data/resident_new.html', {'form': form})

@login_required(login_url='/login/')
def child_new(request, pk):
    household = get_object_or_404(Household, pk=pk)
    if request.method == "POST":
        form = ChildForm(request.POST)
        if form.is_valid():
            child = form.save(commit=False)
            child.household = household
            child.save()
            return redirect('household_list')
    else:
        form = ChildForm()
        args = {}
        args['form'] = form
    return render(request, 'zoom_data/child_new.html', {'form': form})

@login_required(login_url='/login/')
def permissions_new(request, pk):
    resident = get_object_or_404(Resident, pk=pk)
    if request.method == "POST":
        form = PermissionsForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.contact_resident = resident
            contact.date_updated = datetime.now()
            contact.save()
            return redirect('resident_detail', pk=resident.pk)
    else:
        form = PermissionsForm()
        args = {}
        args['form'] = form
    return render(request, 'zoom_data/permissions_new.html', {'form': form, 'resident': resident})

@login_required(login_url='/login/')
def resident_edit(request, pk):
    resident = get_object_or_404(Resident, pk=pk)
    if request.method == "POST":
        form = ResidentForm(request.POST, instance=resident)
        if form.is_valid():
            resident = form.save(commit=False)
            resident.save()
            return redirect('resident_detail', pk=resident.pk)
    else:
        form = ResidentForm(instance=resident)
    return render(request, 'zoom_data/resident_edit.html', {'form': form})

@login_required(login_url='/login/')
def activity_follow_up(request, pk):
    resident = get_object_or_404(Resident, pk=pk)
    return render(request, 'zoom_data/resident_detail.html', {'resident': resident})

@login_required(login_url='/login/')
def household_list(request):
    households = Household.objects.filter(exit_date__isnull = True).order_by('household_name')
    return render(request, 'zoom_data/household_list.html', {'households' : households})

@login_required(login_url='/login/')
def past_household_list(request):
    households = Household.objects.filter(exit_date__isnull = False).order_by('household_name')
    return render(request, 'zoom_data/household_list.html', {'households' : households})