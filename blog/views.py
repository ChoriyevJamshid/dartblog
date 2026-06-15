from django.shortcuts import render

from blog.models import Post



def index_view(request):

    main_post = (
        Post.objects
        .filter(is_published=True)
        .order_by('-published_at').first()
    )

    posts = (
        Post.objects
        .filter(is_published=True)
        .exclude(id=main_post.pk)
    )

    context = {
        'main_post': main_post,
        'posts': posts
    }

    return render(request,
                  template_name='blog/index.html',
                  context=context)



