from django.shortcuts import render, get_object_or_404
from .models import Post
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def post_list(request):
    post_list = Post.published.all()
    paginator = Paginator(post_list, 3)
    page_number = request.GET.get('page', 1)
    try:
        posts = paginator.page(page_number)
    except EmptyPage:
        # if page_number is out of range get last page of results
        posts = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        # if page_number is not an integer get the first page
        posts = paginator.page(1)
    return render(request, 'blog_app/post/list.html', {'posts': posts})

def post_detail(request, year, month, day, post):
    post = get_object_or_404(
        Post,
        slug=post,
        publish__year=year,
        publish__month=month,
        publish__day=day,
        status=Post.Status.PUBLISHED,
    )
    return render(request, 'blog_app/post/detail.html', {'post': post})

#def post_detail(request, id):
#    try:
#        post = Post.published.get(id=id)
#    except Post.DoesNotExist:
#        raise Http404("Post does not exist")
#    return render(request, 'blog_app/post/detail.html', {'post': post})
