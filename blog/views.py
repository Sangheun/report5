from .forms import CommentForm
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post

def index(request):
    post_list = Post.objects.all()
    return render(request, 'blog/index.html', {
        'post_list':post_list,
        })

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {
        'post':post
        })

def comment_new(request, post_pk):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = get_object_or_404(Post, pk=post_pk)
            comment.user = request.user
            comment.save()
            return redirect('blog:post_detail', post_pk)
    else:
        form = CommentForm()
    return render(request, 'blog/comment_form.html', {
        'form':form,
        })