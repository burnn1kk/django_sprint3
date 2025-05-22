from django.shortcuts import render, get_object_or_404
from .models import Post, Category
from django.utils import timezone


def index(request):
    template_name = 'blog/index.html'
    posts = Post.objects.filter(
        is_published=True,
        pub_date__lte=timezone.now(),
        category__is_published=True
    ).order_by('-pub_date')[:5]
    context = {"post_list": posts}
    return render(request, template_name, context)


def post_detail(request, id):
    template_name = 'blog/detail.html'
    post = get_object_or_404(Post.objects.filter(is_published=True,
        pub_date__lte=timezone.now(),
        category__is_published=True),
        id=id)

    context = {"post": post}
    return render(request, template_name, context)


def category_posts(request, category_slug):
    template_name = 'blog/category.html'
    category = get_object_or_404(Category,
        slug=category_slug,
        is_published=True)
    posts = Post.objects.filter(category=category,
        is_published=True,
        pub_date__lte=timezone.now()    
    ).order_by('-pub_date')
    context = {

        'category': category,
        'post_list': posts,
    }
    return render(request, template_name, context)