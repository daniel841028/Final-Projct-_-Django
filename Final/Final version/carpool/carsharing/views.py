from django.shortcuts import render, redirect
from . import models
from .forms import UserForm
from .forms import RegisterForm
import hashlib
from .forms import DriverForm
from .models import DriverList


def main_page(request):
    return render(request, 'main_page.html', {
        'data': "This is main_page",
    })


def index(request):
    return render(request, 'index.html')


def login(request):
    if request.session.get('is_login', None):
        return redirect('/index')

    if request.method == "POST":
        login_form = UserForm(request.POST)
        message = "Please check the content！"
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                user = models.User.objects.get(name=username)
                if user.password == hash_code(password):
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    request.session['user_name'] = user.name
                    return redirect('/index/')
                else:
                    message = "Wrong password！"
            except:
                message = "Username not exist！"
        return render(request, 'login.html', locals())
    login_form = UserForm()
    return render(request, 'login.html', locals())


def register(request):
    if request.session.get('is_login', None):
        return redirect("/index/")
    if request.method == "POST":
        form = RegisterForm(request.POST)
        message = "Please check the content！"
        if form.is_valid():
            name = form.cleaned_data['name']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            email = form.cleaned_data['email']
            if password1 != password2:
                message = "Passwords are not consistant"
                return render(request, 'register.html', locals())
            else:
                same_name_user = models.User.objects.filter(name=name)
                if same_name_user:
                    message = 'username already exists！'
                    return render(request, 'register.html', locals())
                same_email_user = models.User.objects.filter(email=email)
                if same_email_user:
                    message = 'The email was registered！'
                    return render(request, 'register.html', locals())

                new_user = models.User.objects.create()
                new_user.name = name
                new_user.password = hash_code(password1)
                new_user.email = email
                new_user.save()
                return redirect('/login/')
    else:
        form = RegisterForm()
    return render(request, 'register.html', locals())


def logout(request):
    if not request.session.get('is_login', None):
        return redirect("/index/")
    request.session.flush()
    return redirect("/index/")


def hash_code(s, salt='mysite'):
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())
    return h.hexdigest()


def driver_list(request):
    if not request.session.get('is_login', None):
        return redirect("/login/")

    if request.method == "POST":
        form = DriverForm(request.POST)
        if form.is_valid():
            time = form.cleaned_data['time']
            departure = form.cleaned_data['departure']
            destination = form.cleaned_data['destination']
            driver_id = request.session['user_id']
            user = models.User.objects.get(pk=driver_id)

            new_user = models.DriverList.objects.create(
                time=time,
                departure=departure,
                destination=destination,
                driver=user,
            )
            return redirect('/driver_display/')
    else:
        form = DriverForm()
    return render(request, 'driver.html', locals())


def driver_display(request):
    if not request.session.get('is_login', None):
        return redirect("/login/")

    if request.method == "POST":
        models.DriverList.objects.get(id=request.POST.get('id', '')).delete()

    registered_driver = DriverList.objects.all()
    return render(request, 'driver_display.html', locals())


def about(request):
    return render(request, 'about.html', locals())
