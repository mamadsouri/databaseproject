from django.shortcuts import render, redirect
from APP1.models import Student, Professor, University
from django.http import HttpResponse
from .forms import signupStudent, loginform
from django.contrib.auth import login, logout as django_logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import auth


def SignUp(request):

    if request.method == 'POST':

        form = signupStudent(request.POST, request.FILES)

        if form.is_valid():
            Email_s = form.cleaned_data['Email_s']
            degree_of_education_p = form.cleaned_data['degree_of_education_p']
            name_p = form.cleaned_data['name_p']
            uni = form.cleaned_data['uni']
            name_s = form.cleaned_data['name_s']
            family_s = form.cleaned_data['family_s']
            age_s = form.cleaned_data['age_s']
            number_of_student = form.cleaned_data['number_of_student']
            password_s = form.cleaned_data['password_s']
            username_s = form.cleaned_data['username_s']

            Prof_s = Professor.objects.raw('select * from APP1_professor where name_p = %s', [name_p])
            Proff = Prof_s[0]
            university = University.objects.raw('select * from APP1_university where Name = %s', [uni])
            Unii = university[0]
            user = User.objects.create(username=username_s)
            user.set_password(password_s)
            user.save()

            sign = Student.objects.create(Email_s=Email_s, name_s=name_s, family_s=family_s, degree_of_education_p=degree_of_education_p,
                                          number_of_student=number_of_student, age_s=age_s, teacher=Proff, uni=Unii, user=user)
            sign.save()
            return HttpResponse('user hasn been created!')

    else:
        form = signupStudent()
        return render(request, 'accounts/signup.html', {'form': form})
    return HttpResponse('user has not been create!')


def Login(request):
    if request.method == 'POST':

        form = loginform(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = User.objects.raw(f'SELECT * FROM auth_user WHERE username = "{username}"')[0]

            print(user.id)
            if (user.check_password(password)):
                login(request, user)
                return redirect('/')

            # login(request,user)
    else:
        form = loginform()

    return render(request, 'accounts/login.html', {'form': form})


def Logout(request):
    django_logout(request)
    return redirect('/')

