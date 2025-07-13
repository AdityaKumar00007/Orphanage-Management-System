from django.shortcuts import render, redirect
from .models import Child, Donation
from django.http import HttpResponse
from .forms import DonationForm
from datetime import datetime, timedelta
from django.shortcuts import get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'home.html')

def adoption_page(request):
    children = Child.objects.filter(is_adopted=False)  # Only show unadopted children
    return render(request, 'adoption_page.html', {'children': children})

def donate(request): 
    if request.method == 'POST':
        form = DonationForm(request.POST)  # Use the form object directly
        if form.is_valid():
            # Save the form data
            donation = form.save()
            # Pass the donation details to the success page
            return render(request, 'donation_success.html', {
                'name': donation.donor_name,
                'amount': donation.amount
            })
        else:
            # Return errors if form validation fails
            return render(request, 'donate.html', {'form': form})
    else:
        # For GET requests, render an empty form
        form = DonationForm()
        return render(request, 'donate.html', {'form': form})

def adoption(request):
    children = Child.objects.all()
    return render(request, 'adoption.html', {'children': children})    

@login_required(login_url='/login/')
def adopt_child(request, child_id):
    child = get_object_or_404(Child, id=child_id)

    if child.is_adopted:
        return render(request, 'adoption_error.html', {'child': child})
    
    if request.method == "POST":
        # Process the adoption confirmation
        child.is_adopted = True
        child.save()
        
        # Generate appointment details
        appointment_date = datetime.now() + timedelta(days=7)
        formatted_date = appointment_date.strftime("%d-%m-%Y")
        formatted_time = appointment_date.strftime("%H:%M %p")
        
        return render(request, 'adoption_confirmation.html', {
            'child': child,
            'appointment_date': formatted_date,
            'appointment_time': formatted_time,
        })
    else:
        # Show confirmation page first
        return render(request, 'adoption_request.html', {'child': child})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})