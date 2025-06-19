# ================================
#  IMPORTS
# ================================
import ssl
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.timezone import localtime
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import YogaClass, YogaBooking, ZumbaClass, ZumbaBooking, HIITClass, HIITBooking

# ✅ Disable SSL verification (only for development)
ssl._create_default_https_context = ssl._create_unverified_context

# ================================
#  YOGA VIEWS
# ================================

# View to list all Yoga classes
def class_list(request):
    classes = YogaClass.objects.all()
    for c in classes:
        c.local_start_time = localtime(c.start_time)
        c.booked_count = c.total_vacancy - c.available_slots()
    return render(request, 'fitness/class_list.html', {'classes': classes})

# Booking view for a specific Yoga class
@login_required
def book_class(request, class_id):
    yoga_class = get_object_or_404(YogaClass, id=class_id)

    if yoga_class.available_slots() <= 0:
        messages.error(request, "All slots are booked.")
        return redirect('class_list')

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']

        # Create booking record
        YogaBooking.objects.create(
            yoga_class=yoga_class,
            client_name=name,
            client_email=email
        )

        # Email formatting
        local_dt = localtime(yoga_class.start_time)
        formatted_time = local_dt.strftime('%Y-%m-%d %I:%M %p')

        # Send confirmation email
        send_mail(
            'Yoga Class Booking Confirmation',
            f'Dear {name},\n\nYour booking for the yoga class on {formatted_time} (IST) with {yoga_class.instructor} has been confirmed.\n\nThank you!',
            'noreplaymail933@gmail.com',
            [email],
            fail_silently=False,
        )

        messages.success(request, "Booking confirmed. Confirmation sent to email.")
        return redirect('class_list')

    return render(request, 'fitness/book_class.html', {'class': yoga_class})


# ================================
#  ZUMBA VIEWS
# ================================

# View to list all Zumba classes
def zumba_class_list(request):
    classes = ZumbaClass.objects.all()
    for c in classes:
        c.local_start_time = localtime(c.start_time)
        c.booked_count = c.total_vacancy - c.available_slots()
    return render(request, 'fitness/zumba_class_list.html', {'classes': classes})

# Booking view for Zumba class
@login_required
def book_zumba_class(request, class_id):
    zumba_class = get_object_or_404(ZumbaClass, id=class_id)

    if zumba_class.available_slots() <= 0:
        messages.error(request, "All slots are booked.")
        return redirect('zumba_class_list')

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']

        ZumbaBooking.objects.create(
            zumba_class=zumba_class,
            client_name=name,
            client_email=email
        )

        local_dt = localtime(zumba_class.start_time)
        formatted_time = local_dt.strftime('%Y-%m-%d %I:%M %p')

        send_mail(
            'Zumba Class Booking Confirmation',
            f'Dear {name},\n\nYour booking for the Zumba class on {formatted_time} (IST) with {zumba_class.instructor} has been confirmed.\n\nThank you!',
            'noreplaymail933@gmail.com',
            [email],
            fail_silently=False,
        )

        messages.success(request, "Booking confirmed.")
        return redirect('zumba_class_list')

    return render(request, 'fitness/book_zumba_class.html', {'class': zumba_class})


# ================================
#  HIIT VIEWS
# ================================

# View to list all HIIT classes
def hiit_class_list(request):
    classes = HIITClass.objects.all()
    for c in classes:
        c.local_start_time = localtime(c.start_time)
        c.booked_count = c.total_vacancy - c.available_slots()
    return render(request, 'fitness/hiit_class_list.html', {'classes': classes})

# Booking view for HIIT class
@login_required
def book_hiit_class(request, class_id):
    hiit_class = get_object_or_404(HIITClass, id=class_id)

    if hiit_class.available_slots() <= 0:
        messages.error(request, "All slots are booked.")
        return redirect('hiit_class_list')

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']

        HIITBooking.objects.create(
            hiit_class=hiit_class,
            client_name=name,
            client_email=email
        )

        local_dt = localtime(hiit_class.start_time)
        formatted_time = local_dt.strftime('%Y-%m-%d %I:%M %p')

        send_mail(
            'HIIT Class Booking Confirmation',
            f'Dear {name},\n\nYour booking for the HIIT class on {formatted_time} (IST) with {hiit_class.instructor} has been confirmed.\n\nThank you!',
            'noreplaymail933@gmail.com',
            [email],
            fail_silently=False,
        )

        messages.success(request, "Booking confirmed.")
        return redirect('hiit_class_list')

    return render(request, 'fitness/book_hiit_class.html', {'class': hiit_class})


# ================================
#  AUTH VIEWS
# ================================

# User Registration
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created! Please log in.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'fitness/register.html', {'form': form})

# Login
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('class_list')
    else:
        form = AuthenticationForm()
    return render(request, 'fitness/login.html', {'form': form})

# Logout
def logout_view(request):
    logout(request)
    return redirect('login')


# ================================
#  HOME VIEW
# ================================

def home(request):
    return render(request, 'fitness/home.html')
