from django.shortcuts import render
from django.views import generic
from .models import Post

# Create your views here.

class PostListView(generic.ListView):
    model = Post
    template_name = 'forum/index.html'  # Updated template name
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 3

    def get_queryset(self):
        return Post.objects.filter(status=1).order_by('-date_posted')