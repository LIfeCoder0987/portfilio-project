from django.shortcuts import render, get_object_or_404
from .models import Blog

def all_blogs(request):
	blogs = Blog.objects
	return render(request, 'blog/all_blogs.html', {'blogs':blogs})

def blog_detail(request, blog_id):
	blog_detail = get_object_or_404(Blog, pk=blog_id)
	return render(request, 'blog/blog_detail.html', {'blog_detail': blog_detail})
