from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from myapp.forms import signUpForm, signInForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def sign_up(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = signUpForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'User registered successfully!')
                return redirect('sign_in')
        else:
            form = signUpForm()

        context = {
            'signupForm': form
        } 
        return render(request, 'signup.html', context)
    else:
        return redirect('dashboard')




def sign_in(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = signInForm(request=request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']

                user = authenticate(username=username, password=password)

                if user is not None:
                    login(request, user)
                    # messages.success(request, 'User logged in successfully!')

                    return redirect('home')
        else:
            form = signInForm()

        context = {'signinForm':form}

        return render(request, 'signin.html', context)
    else:
        return redirect('dashboard')


@login_required(login_url='sign_in')
def sign_out(request):
    logout(request)
    messages.success(request, 'User logged out successfully!')
    return redirect('sign_in')


