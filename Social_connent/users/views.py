from django.shortcuts import render, redirect, get_object_or_404
from .forms import registrationForm
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from posts.models import Post, Comment
from .models import User

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
    user_posts = Post.objects.filter(author = request.user).order_by('-created_at')
    comments = Post.comment_set.all()
    return render(request, 'users/profile.html',{'user_posts':user_posts, 'comments':comments})