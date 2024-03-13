from django.shortcuts import render, redirect
from django.contrib.auth import login,authenticate
from .forms import RegistrationForm, UserProfileForm
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import LoginForm


def register(request):
    if request.method == 'POST':
        user_form = RegistrationForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            login(request, user)
            return redirect('login')  # Use the name of the URL pattern for the index view
    else:
        user_form = RegistrationForm()
        profile_form = UserProfileForm()

    return render(request, 'register.html', {'user_form': user_form, 'profile_form': profile_form})

@login_required
def profile(request):
    user_profile = UserProfile.objects.get(user=request.user)
    return render(request, 'profile.html', {'user_profile': user_profile})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile')  # Redirect to home page after successful login
            else:
                # Authentication failed
                # You can add error handling here, like displaying an error message
                pass
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})