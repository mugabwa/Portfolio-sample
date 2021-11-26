from django.shortcuts import render

from blog.forms import CommentForm
from .models import Comment, Post

# Create your views here.
def blog_index(request):
    posts = Post.objects.all().order_by('-created_on')
    context = {
        'posts':posts,
        'blog_page': 'active'
    }
    return render(request,'blog_index.html', context)

def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid(): ## Checks if all fields have been entered correctly
            comment = Comment(
                author = form.cleaned_data['author'],
                body = form.cleaned_data['body'],
                post = post
            )
            comment.save()
    comments = Comment.objects.filter(post=post)
    context = {
        'post': post,
        'comments':comments,
        'form': form,
        'blog_page': 'active'
    }
    return render(request, 'blog_details.html', context)

def blog_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains = category
    ).order_by('-created_on')   ## filter for conditions
    context = {
        'category': category,
        'posts': posts,
        'blog_page': 'active'
    }
    return render(request, 'blog_category.html', context)