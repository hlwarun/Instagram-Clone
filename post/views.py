from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from post.models import Post, Tag
from follow.models import Stream
from post.forms import CreatePostForm

# Create your views here.

@login_required
def feeds(request):
    user = request.user
    posts = Stream.objects.filter(user=user)
    post_list = []

    for post in posts:
        post_list.append(post.post_id)

    all_posts = Post.objects.filter(id__in=post_list).all().order_by('-created_at')

    context = {'title': 'Feeds', 'all_posts':all_posts}
    return render(request, 'feed.html', context)

@login_required
def create_post(request):
    user = request.user.id
    all_tags = []

    if request.method == 'POST':
        form = CreatePostForm(request.POST, request.FILES)

        if form.is_valid():
            photo = form.cleaned_data.get('photo')
            caption = form.cleaned_data.get('caption')
            location = form.cleaned_data.get('location')
            tags = form.cleaned_data.get('tags')

            tags_list = list(tags.split(','))
            for tag in tags_list:
                t, created_at = Tag.objects.get_or_create(title=tag)
                all_tags.append(t)

            p, created_at = Post.objects.get_or_create(photo=photo, caption=caption, user_id=user)
            p.tags.set(all_tags)
            p.save()
            return redirect('post:home')
    else:
        form = CreatePostForm()

    context = {'title':'Create New Post', 'form':form, 'user':request.user}
    return render(request, 'create-post.html', context)
