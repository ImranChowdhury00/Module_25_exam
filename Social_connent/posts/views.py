from django.shortcuts import render, get_object_or_404 ,redirect, HttpResponse
from .models import Post
from .forms import postForm
from django.contrib.auth.decorators import login_required

def home(request):
    posts = Post.objects.all().order_by("-created_at")
    return render(request, 'posts/home.html', {'posts':posts})

# @login_required
# def create_post(request):
#     form = 

@login_required
def post_edit(request ,pk):
    post = get_object_or_404(Post, id= pk, author= request.user)

    if request.method == 'POST':
        form = postForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = postForm(instance=post)
        return render(request,'posts/edit_post.html',{'form':form})
    
@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, id=pk, author= request.user)

    if post.author!= request.user:
        return HttpResponse("You are not authorised to delete this")
    post.delete()
    return redirect("profile")
