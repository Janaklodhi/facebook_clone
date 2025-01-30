from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from .models import UserProfile

from django.contrib.auth import authenticate, login

def signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        date_of_birth = request.POST['date_of_birth']
        gender = request.POST['gender']
        phone_number = request.POST['phone_number']
        password = request.POST['password']
        if User.objects.filter(email=email).exists():
            return render(request, 'signup.html', {'error': 'Email already exists'})
        # Create the User object (Django's built-in User model)
        user = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            username=email,
            password=make_password(password)  # Hashing the password
        )

        # Create the UserProfile object and link it to the User
        user_profile = UserProfile.objects.create(
            user=user,
            date_of_birth=date_of_birth,
            phone_number=phone_number
        )

        # Redirect to a success page after signup
        return redirect('login')  # Redirect to the user_login page

    return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        email_or_phone = request.POST.get('email_or_phone')
        password = request.POST.get('password')
        user = None
        if User.objects.filter(email=email_or_phone).exists():
            user = User.objects.get(email=email_or_phone)
        elif UserProfile.objects.filter(phone_number=email_or_phone).exists():
            user_profile = UserProfile.objects.get(phone_number=email_or_phone)
            user = user_profile.user
        if user is not None and user.check_password(password):
            login(request)
            return redirect('home')
        print("Invalid credentials")
        return render(request, 'login.html', {'error': 'Invalid email/phone or password'})

    return render(request, 'login.html')



def home(request):
    return render(request, 'home.html')



# def signup_success(request):
#     return render(request, 'signup_success.html')
