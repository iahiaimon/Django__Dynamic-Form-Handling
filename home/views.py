from django.shortcuts import render , redirect
from django.http import HttpResponse
from login import views
from login import models

# Create your views here.


def home(request):
    users = models.User.objects.all()
    return render(request, "index.html", {"users": users})


def update_user(request , id):

    user = models.User.objects.get(id = id)
    form = views.forms.LoginForm(instance=user)
    # form = views.forms.LoginForm()

    if request.method == 'POST':
        form = views.forms.LoginForm(request.POST , request.FILES , instance=user )
        form.save()
        return redirect('home')

    return render(request, "login.html", {"form": form , "edit" : True})


def delete_user(request , id):
    user = models.User.objects.get(id = id)
    user.delete()
    return redirect('home')