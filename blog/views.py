from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post, Category


# CBV 방식
class PostList(ListView):
    model = Post
    ordering = '-pk'
    #template_name ='blog/index.html'

def get_context_data(self, **kwargs):
    context = super(PostList, self).get_context_data()
    context['categories'] = Category.objects.all()
    context['no_category_post_count'] = Post.objects.filter(category=None).count()
    return context


def category_page(request, category_name):
    category = Category.objects.get(category=category_name)
    post_list = Post.objects.filter(category=category)

    return render(
        request,
        'blog/post_list.html',
        {
            'post_list' : post_list,
            'category' : Category.objects.all(),
            'no_category_post_count' : Post.objects.filter(category=None).count(),
            'category_name' : category_name,
            'category' : category,
        }
    )


class PostDetail(DetailView):
    model = Post

""" FBV 방식
def index(request):

    posts = Post.objects.all().order_by('-pk')

    return render(
        request,
        'blog/index.html',
        {
            'posts' : posts,
        }
    )


def single_post_page(request, pk):
        post = Post.objects.get(pk=pk)

        return render(
           request,
        'blog/single_post_page.html',
        {
            'posts' : post,
        }
    ) 
    """