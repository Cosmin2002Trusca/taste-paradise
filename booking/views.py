from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout
from django.contrib import messages
from .models import Booking, Table
from .models import BookingForm
from django.core.exceptions import ValidationError
# Create your views here.

def homepage(request):
    return render(request, 'booking/home_page.html',)

def login_view(request):
    if request.user.is_authenticated:
        return redirect('homepage')
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('homepage')
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'booking/login.html', {'form': form})

def signup_view(request):
    if request.user.is_authenticated:
        return redirect('homepage')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user immediately after sign up
            return redirect('homepage')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = UserCreationForm()
    return render(request, 'booking/signup.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('homepage')

from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Table, Booking
from django.core.exceptions import ValidationError

@login_required
def book_table(request):
    if request.method == 'POST':
        customer_name = request.POST.get('customer_name')
        customer_email = request.POST.get('customer_email')
        customer_phone = request.POST.get('customer_phone')
        booking_date_str = request.POST.get('booking_date')  
        booking_time_str = request.POST.get('booking_time') 
        table_id = request.POST.get('table')
        special_request = request.POST.get('special_request')

        # Validate the selected table
        try:
            table = Table.objects.get(id=table_id)
        except Table.DoesNotExist:
            messages.error(request, "The selected table does not exist.")
            return redirect('book_table')

        # Convert number_of_guests to integer
        try:
            number_of_guests = int(request.POST.get('number_of_guests'))
        except (ValueError, TypeError):
            messages.error(request, "Number of guests must be a valid number.")
            return redirect('book_table')

        # Convert booking_date from string to date object
        try:
            booking_date = datetime.strptime(booking_date_str, "%Y-%m-%d").date()
        except ValueError:
            messages.error(request, "Booking date must be in YYYY-MM-DD format.")
            return redirect('book_table')

        # Convert booking_time from string to time object
        try:
            booking_time = datetime.strptime(booking_time_str, "%H:%M").time()
        except ValueError:
            messages.error(request, "Booking time must be in HH:MM format.")
            return redirect('book_table')

        # Create the booking instance but do not save yet
        booking = Booking(
            user=request.user,
            customer_name=customer_name,
            customer_email=customer_email,
            customer_phone=customer_phone,
            booking_date=booking_date,  
            booking_time=booking_time,  
            number_of_guests=number_of_guests,
            table=table,
            special_request=special_request
        )

        # Run model validation
        try:
            booking.clean()
            booking.save()
            messages.success(request, "Your table has been successfully booked!")
            return redirect('homepage')  # Redirect to your homepage or success page
        except ValidationError as e:
            messages.error(request, e)

    tables = Table.objects.all()  # Get all available tables
    return render(request, 'booking/book_table.html', {'tables': tables})

def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user).order_by('booking_date', 'booking_time')
    return render(request, 'booking/my_bookings.html', {'bookings': bookings})

def delete_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    
    if request.method == "POST":
        booking.delete()
        messages.success(request, "Your booking has been canceled.")
        return redirect('my_bookings')

    return redirect('my_bookings')

def edit_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    
    if request.method == "POST":
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            messages.success(request, "Booking updated successfully!")
            return redirect('my_bookings')
    else:
        form = BookingForm(instance=booking)

    return render(request, 'booking/edit_booking.html', {'form': form})