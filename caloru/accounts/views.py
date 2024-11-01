from django.shortcuts import redirect, render

from .forms import RegisterForm

# Create your views here.


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
        return render(request, "registration/register.html", {"form": form})
    form = RegisterForm()
    return render(request, "registration/register.html", {"form": form})
