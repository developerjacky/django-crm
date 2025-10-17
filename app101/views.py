from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import People
from .forms import PeopleForm


def index(request):
    data = People.objects.all()
    context = { 'data' : data, }
    return render(request, 'app101/index.html', context)

def detail(request, people_id):
    data = People.objects.get(pk=people_id)
    context = {
          'data' : data,
    }
    return render(request, 'app101/detail.html', context)

def add_people(request):
    """Add a new customer"""
    if request.method == 'POST':
        form = PeopleForm(request.POST)
        if form.is_valid():
            people = form.save()
            return redirect('index')
    else:
        form = PeopleForm()
    
    return render(request, 'app101/people_form.html', {
        'form': form,
        'title': 'Add New Customer'
    })


def edit_people(request, people_id):
    """Edit an existing people"""
    people = get_object_or_404(People, id=people_id)
    
    if request.method == 'POST':
        form = PeopleForm(request.POST, instance=people)
        if form.is_valid():
            people = form.save()
            return redirect('index')
    else:
        form = PeopleForm(instance=people)
    
    return render(request, 'app101/people_form.html', {
        'form': form,
        'title': 'Edit People',
        'people': people
    })

def delete_people(request, people_id):
    """Delete a people"""
    people = get_object_or_404(People, id=people_id)
    if request.method == 'POST':
        people.delete()
        return redirect('index')
    # Handle GET request - show confirmation page
    return render(request, 'app101/confirm_delete.html', {'people': people})


