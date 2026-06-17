from django.shortcuts import render

from blog.models import Post, Category


def post_list_view(request, category_id=None):
    categories = Category.objects.all()
    posts = Post.objects.filter(is_published=True)

    if category_id is None:
        category_id = (
            Category.objects
            .values_list('id', flat=True)
            .first())

    posts = posts.filter(category__id=category_id)

    main_post = posts[0] if posts else None
    posts = posts.exclude(id=main_post.pk if main_post else 0)

    context = {
        'categories': categories,
        'posts': posts,
        'main_post': main_post,
        'selected_category': category_id,
    }

    # print(context)

    return render(request,
                  template_name='blog/index.html',
                  context=context)
