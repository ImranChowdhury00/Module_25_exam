from django.shortcuts import render, redirect, get_object_or_404 , HttpResponse
from .forms import registrationForm
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from posts.models import Post, Comment
from .models import User
from posts.forms import postForm


def user_registration(request):
    if request.method == "POST":
        form = registrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = registrationForm()
    return render(request, 'users/registration.html', {'form':form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data= request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username= username, password= password)
            login(request, user)
            return redirect('profile')
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form':form})

@login_required    
def user_logout(request):
    logout(request)
    return redirect('user_login')

@login_required
def profile(request):
    if request.method == "POST":
        form = postForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('profile')
        else:
            return HttpResponse("not valid!!")
    else:
        user_posts = Post.objects.filter(author = request.user).order_by('-created_at')
        return render(request, 'users/profile.html',{'user_posts':user_posts})
    