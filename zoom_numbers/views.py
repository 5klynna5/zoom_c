from django.shortcuts import render, get_object_or_404, redirect
from .models import YMCA, FoodShelf
from .forms import YMCAForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def monthly_numbers(request):
	return render(request, 'zoom_numbers/monthly_numbers.html')

@login_required(login_url='/login/')
def ymca_visits(request):
	visits = YMCA.objects.all()
	return render(request, 'zoom_numbers/ymca_visits.html', {'visits': visits})

@login_required(login_url='/login/')
def food_shelf_visits(request):
	visits = FoodShelf.objects.all()
	return render(request, 'zoom_numbers/food_shelf_visits.html', {'visits': visits})

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
    return render(request, 'zoom_numbers/ymca_edit.html', {'form': form})