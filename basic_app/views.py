from django.shortcuts import render

from basic_app.forms import UserForm
from basic_app.forms import UserProfileInfoForm

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.

app_name = 'basic_app'


def index(request):
    print('request; ', request)
    return render(request, 'basic_app/index.html')


def info(request):
    return render(request, 'basic_app/info.html')


def register(request):
    registered = False

    if request.method == 'POST':

        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        print('data: ', request.POST)

        if user_form.is_valid() \
                and profile_form.is_valid() \
                and user_form.cleaned_data['password'] == user_form.cleaned_data['confirm_password']:

            print('files: ', request.FILES)

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                print('Found file: ', request.FILES['profile_pic'])
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True

            return render(request, 'basic_app/registration.html', {
                'user_form': user_form,
                'profile_form': profile_form,
                'registered': registered
            })

        elif user_form.cleaned_data['password'] != user_form.cleaned_data['confirm_password']:
            user_form.add_error('confirm_password', 'The passwords do not match')
            return render(request, 'basic_app/registration.html', {
                'user_form': user_form,
                'profile_form': profile_form,
                'registered': registered
            })
        elif len(user_form.cleaned_data['password']) < 5:
            user_form.add_error('password', 'The password length must be at least 6')
            return render(request, 'basic_app/registration.html', {
                'user_form': user_form,
                'profile_form': profile_form,
                'registered': registered
            })
        else:

            print('user_form.errors: ', user_form.errors)
            print('profile_form.errors: ', profile_form.errors)
            return render(request, 'basic_app/registration.html', {
                'user_form': user_form,
                'profile_form': profile_form,
                'registered': registered
            })
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
        return render(request, 'basic_app/registration.html', {
            'user_form': user_form,
            'profile_form': profile_form,
            'registered': registered
        })


def login_user(request):
    errors = []
    if request.method == 'POST':
        username, password = request.POST.get('username'), request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user and user.is_active:
            login(request, user)
            print('user: ', user)
            return render(request, 'basic_app/login.html', {'errors': errors, 'user': user})
        else:
            errors.append('User was not found, check your username or password')
            return render(request, 'basic_app/login.html', {'errors': errors})
    else:
        return render(request, 'basic_app/login.html', {'errors': errors})


@login_required
def user_logout(request):
    logout(request)
    return render(request, 'basic_app/login.html')
