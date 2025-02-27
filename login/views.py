from django.shortcuts import render ,redirect
from django.http import HttpResponse 
from . import models , forms
# Create your views here.

def loginform(request):
    form = forms.LoginForm()

    if request.method == 'POST':
        form = forms.LoginForm(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
            # return HttpResponse('Login Success')
    
    return render(request , 'login.html' , {'form':form})







        #     username = form.cleaned_data['username']
        #     password = form.cleaned_data['password']
        #     user = authenticate(username=username, password=password)
        #     if user is not None:
        #         login(request, user)
        #         return redirect('home')
        #     else:
        #         return render(request, 'login.html', {'form': form, 'error': 'Invalid username or password'})
        # return render(request, 'login.html', {'form': form})
                                                      
