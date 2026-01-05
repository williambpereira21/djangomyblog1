# djangomyblog\blog\views.py

from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from blog.models import Post, Comment
from .forms_comment import CommentForm


def home(request):
    posts = (
        Post.objects
        .filter(status='ON')
        .select_related('user')
        .order_by('-created_at')
    )
    return render(request, "blog/home.html", {"posts": posts})


def about(request):
    return render(request, "blog/about.html")


@login_required
def profile(request):
    return render(request, "blog/profile.html")


def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = CustomUserCreationForm()

    return render(request, "registration/signup.html", {"form": form})


# Função post_detail atualizada com comentários
def post_detail(request, id):
    post = get_object_or_404(Post, id=id, status='ON')
    comments = Comment.objects.filter(post=post, status='ON').order_by('-created_at')

    if request.method == "POST" and request.user.is_authenticated:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            return redirect('post_detail', id=post.id)
    else:
        form = CommentForm()

    return render(request, 'blog/post_detail.html', {
        'post': post,
        'comments': comments,
        'form': form
    })


@login_required
def new_post(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")

        if title and content:
            Post.objects.create(
                title=title,
                content=content,
                user=request.user,
                status='ON'
            )
            return redirect("home")

    return render(request, "blog/new_post.html")


@login_required
def delete_post(request, id):
    post = get_object_or_404(Post, id=id, status='ON')

    if post.user != request.user:
        return redirect('home')

    post.status = 'DEL'
    post.save(update_fields=['status'])

    return redirect('home')


@login_required
def edit_post(request, id):
    post = get_object_or_404(Post, id=id, status='ON')

    # só o dono pode editar
    if post.user != request.user:
        return redirect('home')

    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")

        if title and content:
            post.title = title
            post.content = content
            post.save(update_fields=['title', 'content'])
            return redirect('post_detail', id=post.id)

    return render(request, 'blog/edit_post.html', {
        'post': post
    })
