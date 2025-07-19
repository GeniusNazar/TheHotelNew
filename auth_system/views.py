from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from auth_system.forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm


def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("index")

    else:
        form = CustomUserCreationForm()
        messages.error(request, message="Помилка")

    return render(
        request,
        template_name="auth_system/register.html",
        context={"form": form}
    )


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("index")
            else:
                messages.error(request, message="Неправильний логін або пароль")

    else:
        form = AuthenticationForm()


        return render(
            request,
            template_name="auth_system/login.html",
            context={"form": form}
        )




