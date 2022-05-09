from django.shortcuts import render, redirect
from .models import BlogPost
from .forms import BlogPostForm
from django.contrib.auth.decorators import login_required
from django.http import Http404


def check_blog_owner(request, blog):
    """Protect from edit foreign blog"""
    if blog.user != request.user:
        raise Http404


def index(request):
    """Main page"""
    blogs = BlogPost.objects.order_by('-date_added')
    context = {'blogs': blogs, 'request': request}
    return render(request, 'Blogs/index.html', context)


@login_required
def new_blog(request):
    """Redirect to create page with form"""
    if request.method != 'POST':
        form = BlogPostForm()
    else:
        form = BlogPostForm(data=request.POST)
        if form.is_valid():
            new_personal_blog = form.save(commit=False)
            new_personal_blog.user = request.user
            new_personal_blog.save()
            return redirect('Blogs:index')
    context = {'form': form}
    return render(request, 'Blogs/new_blog.html', context)


@login_required
def edit_all_blogs(request):
    """Redirect to user blogs page"""
    blogs = BlogPost.objects.filter(user_id=request.user).order_by('-date_added')
    context = {'blogs': blogs}
    return render(request, 'Blogs/edit_all_blogs.html', context)


@login_required
def edit_blog(request, blog_id):
    """Redirect to user blog page with edit form"""
    blog = BlogPost.objects.get(id=blog_id)
    check_blog_owner(request, blog)
    if request.method != 'POST':
        form = BlogPostForm(instance=blog)
    else:
        form = BlogPostForm(instance=blog, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('Blogs:index')
    context = {'blog': blog, 'form': form}
    return render(request, 'Blogs/edit_blog.html', context)
