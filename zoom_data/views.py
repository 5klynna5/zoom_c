from django.shortcuts import render, get_object_or_404, redirect
from .models import Resident, Goal, Progress, Household, Child, Activity, ExitInterview, FollowUp, Attendance, Annual, CaseNotes
from .forms import GoalForm, ResidentForm, ProgressForm, HouseholdForm, ChildForm, PermissionsForm, ActivityForm, ActivitySurveyForm, AttendanceForm, ChildAttendanceForm, ExitForm, FollowUpForm, AnnualForm, CaseNotesForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.utils.timezone import datetime
from django.db.models import Avg

@login_required(login_url='/login/')
def home(request):
    households = Household.objects.filter(exit_date__isnull=True)
    households_one_bedroom = households.filter(unit_type = 'SH_ONE_BEDROOM')
    households_marif = households.filter(unit_type = 'SH_MARIF')
    households_studio = households.filter(unit_type = 'SH_STUDIO')
    resident_list = [resident.pk for resident in Resident.objects.all() if (resident.household in households)]
    residents = Resident.objects.filter(pk__in=resident_list)
    residents_male = residents.filter(gender = 'MALE')
    residents_female = residents.filter(gender = 'FEMALE')
    child_list = [child.pk for child in Child.objects.all() if (child.household in households)]
    children = Child.objects.filter(pk__in=child_list)
    children_male = children.filter(gender = 'MALE')
    children_female = children.filter(gender = 'FEMALE')
    residents_one_bedroom_list =  [resident.pk for resident in Resident.objects.all() if (resident.household in households_one_bedroom)]
    residents_one_bedroom = Resident.objects.filter(pk__in=residents_one_bedroom_list)
    residents_marif_list =  [resident.pk for resident in Resident.objects.all() if (resident.household in households_marif)]
    residents_marif = Resident.objects.filter(pk__in=residents_marif_list)
    residents_studio_list =  [resident.pk for resident in Resident.objects.all() if (resident.household in households_studio)]
    residents_studio = Resident.objects.filter(pk__in=residents_studio_list)
    children_one_bedroom_list =  [child.pk for child in Child.objects.all() if (child.household in households_one_bedroom)]
    children_one_bedroom = Child.objects.filter(pk__in=children_one_bedroom_list)
    children_marif_list =  [child.pk for child in Child.objects.all() if (child.household in households_marif)]
    children_marif = Child.objects.filter(pk__in=children_marif_list) 
    res_stays_sum = 0
    for item in residents:
        res_stays_sum = res_stays_sum + item.length_of_stay
    ave_stays_residents = res_stays_sum / residents.count()
    household_stays_sum = 0
    for item in households:
        household_stays_sum = household_stays_sum + item.length_of_stay
    ave_stays_households = household_stays_sum / households.count()
    child_stays_sum = 0
    for item in children:
        child_stays_sum = child_stays_sum + item.length_of_stay
    ave_stays_children = child_stays_sum / children.count()
    #vols_combined = dict(Counter(total_vols_month) + Counter(group_vols_month))
    return render(request,'zoom_data/home.html', {'ave_stays_children' : ave_stays_children, 'ave_stays_residents': ave_stays_residents, 'ave_stays_households' : ave_stays_households, 'households': households, 'households_one_bedroom': households_one_bedroom, 'households_marif': households_marif, 'households_studio': households_studio, 'residents' : residents, 'children' : children, 'residents_male' : residents_male, 'residents_female': residents_female, 'children_male': children_male, 'children_female' : children_female, 'residents_one_bedroom': residents_one_bedroom, 'children_one_bedroom': children_one_bedroom, 'residents_marif': residents_marif, 'children_marif': children_marif, 'residents_studio' : residents_studio})

@login_required(login_url='/login/')
def activities_list(request):
	activities = Activity.objects.all()
	return render(request, 'zoom_data/activities_list.html', {'activities' : activities})

@login_required(login_url='/login/')
def activity_detail(request, pk):
    activity = get_object_or_404(Activity, pk=pk)
    return render(request, 'zoom_data/activity_detail.html', {'activity': activity})

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
def follow_up_new(request, pk):
    attendance = get_object_or_404(Attendance, pk=pk)
    if request.method == "POST":
        form = FollowUpForm(request.POST)
        if form.is_valid():
            followup = form.save(commit=False)
            followup.attendance = attendance
            followup.save()
            return redirect('activity_list')
    else:
        form = FollowUpForm()
    return render(request, 'zoom_data/follow_up_new.html', {'form': form})

@login_required(login_url='/login/')
def annual_new(request, pk):
    resident = get_object_or_404(Resident, pk=pk)
    if request.method == "POST":
        form = AnnualForm(request.POST)
        if form.is_valid():
            annual = form.save(commit=False)
            annual.resident = resident
            annual.save()
            return redirect('resident_detail', pk = resident.pk)
    else:
        form = AnnualForm()
    return render(request, 'zoom_data/annual_new.html', {'form': form})

@login_required(login_url='/login/')
def case_notes_new(request, pk):
    resident = get_object_or_404(Resident, pk=pk)
    if request.method == "POST":
        form = CaseNotesForm(request.POST)
        if form.is_valid():
            casenotes = form.save(commit=False)
            casenotes.resident = resident
            casenotes.save()
            return redirect('resident_detail', pk = resident.pk)
    else:
        form = CaseNotesForm()
    return render(request, 'zoom_data/case_notes_new.html', {'form': form})

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
def activity_survey_new(request, pk):
    activity = get_object_or_404(Activity, pk=pk)
    if request.method == "POST":
        form = ActivitySurveyForm(request.POST)
        if form.is_valid():
            activitysurvey = form.save(commit=False)
            activitysurvey.activity = activity
            activitysurvey.save()
            return redirect('activity_detail', pk = activity.pk)
    else:
        form = ActivitySurveyForm()
        args = {}
        args['form'] = form
    return render(request, 'zoom_data/activity_survey_new.html', {'form': form, 'activity': activity})

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
def household_edit(request, pk):
    household = get_object_or_404(Household, pk=pk)
    if request.method == "POST":
        form = HouseholdForm(request.POST, instance=household)
        if form.is_valid():
            household = form.save(commit=False)
            household.save()
            return redirect('household_list')
    else:
        form = HouseholdForm(instance=household)
    return render(request, 'zoom_data/household_edit.html', {'form': form})


@login_required(login_url='/login/')
def household_list(request):
    households = Household.objects.filter(exitinterview = None).order_by('household_name')
    return render(request, 'zoom_data/household_list.html', {'households' : households})

@login_required(login_url='/login/')
def past_household_list(request):
    households = Household.objects.filter(exitinterview__isnull = False).order_by('household_name')
    return render(request, 'zoom_data/past_household_list.html', {'households' : households})

@login_required(login_url='/login/')
def exit_interview_view(request, pk):
    exit_interview = get_object_or_404(ExitInterview, pk=pk)
    return render(request, 'zoom_data/exit_interview_view.html', {'exit_interview' : exit_interview})

@login_required(login_url='/login/')
def exit_new(request, pk):
    household = get_object_or_404(Household, pk=pk)
    if request.method == "POST":
        form = ExitForm(request.POST)
        if form.is_valid():
            exitinterview = form.save(commit=False)
            exitinterview.household = household
            exitinterview.save()
            return redirect('household_list')
    else:
        form = ExitForm()
        args = {}
        args['form'] = form
    return render(request, 'zoom_data/exit_new.html', {'form': form})