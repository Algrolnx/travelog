from django.shortcuts import render, redirect, get_object_or_404
from users_app.models import Profile
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            # Перевіряємо та створюємо профіль, якщо потрібно
            if not hasattr(request.user, 'profile'):
                Profile.objects.create(user=request.user)
            post.author = request.user.profile
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()

    return render(request, 'blog/create_post.html', {'form': form})
