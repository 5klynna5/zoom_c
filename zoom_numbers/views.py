from django.shortcuts import render, get_object_or_404, redirect
from .models import YMCA, FoodShelf, PoliceCalls, QuestionMonth
from .forms import YMCAForm, FoodShelfForm, PoliceCallsForm, QuestionMonthForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def monthly_numbers(request):
	return render(request, 'zoom_numbers/monthly_numbers.html')

@login_required(login_url='/login/')
def ymca_visits(request):
	visits = YMCA.objects.all().order_by('-pk')
	return render(request, 'zoom_numbers/ymca_visits.html', {'visits': visits})

@login_required(login_url='/login/')
def police_calls(request):
	calls = PoliceCalls.objects.all().order_by('-pk')
	return render(request, 'zoom_numbers/police_calls.html', {'calls': calls})

@login_required(login_url='/login/')
def food_shelf_visits(request):
	visits = FoodShelf.objects.all().order_by('-pk')
	return render(request, 'zoom_numbers/food_shelf_visits.html', {'visits': visits})

@login_required(login_url='/login/')
def questions_of_month(request):
	questions = QuestionMonth.objects.all().order_by('-pk')
	return render(request, 'zoom_numbers/questions_of_month.html', {'questions': questions})

@login_required(login_url='/login/')
def ymca_new(request):
    if request.method == "POST":
        form = YMCAForm(request.POST)
        if form.is_valid():
            ymca = form.save(commit=False)
            ymca.save()
            return redirect('ymca_visits')
    else:
        form = YMCAForm()
    return render(request, 'zoom_numbers/ymca_new.html', {'form': form})

@login_required(login_url='/login/')
def food_shelf_new(request):
    if request.method == "POST":
        form = FoodShelfForm(request.POST)
        if form.is_valid():
            foodshelf = form.save(commit=False)
            foodshelf.save()
            return redirect('food_shelf_visits')
    else:
        form = FoodShelfForm()
    return render(request, 'zoom_numbers/food_shelf_new.html', {'form': form})

@login_required(login_url='/login/')
def police_calls_new(request):
    if request.method == "POST":
        form = PoliceCallsForm(request.POST)
        if form.is_valid():
            policecalls = form.save(commit=False)
            policecalls.save()
            return redirect('police_calls')
    else:
        form = PoliceCallsForm()
    return render(request, 'zoom_numbers/police_calls_new.html', {'form': form})

@login_required(login_url='/login/')
def question_month_new(request):
    if request.method == "POST":
        form = QuestionMonthForm(request.POST)
        if form.is_valid():
            questionmonth = form.save(commit=False)
            questionmonth.save()
            return redirect('questions_of_month')
    else:
        form = QuestionMonthForm()
    return render(request, 'zoom_numbers/question_month_new.html', {'form': form})

@login_required(login_url='/login/')
def question_month_detail(request, pk):
    question_month = get_object_or_404(QuestionMonth, pk=pk)
    return render(request, 'zoom_numbers/question_month_detail.html', {'question_month': question_month})