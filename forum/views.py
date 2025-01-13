from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.views import View
from django.db import models  # Import models
from .models import Post, ContactMessage
from .forms import ContactUsForm

# Create your views here.

class PostListView(generic.ListView):
    model = Post
    template_name = 'forum/index.html'  # Updated template name
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 3

    def get_queryset(self):
        queryset = Post.objects.filter(status=1).order_by('-date_posted')
        for post in queryset:
            post.total_votes = post.ratings.aggregate(total=models.Sum('vote'))['total'] or 0
        return queryset

class ContactUsView(View):
    template_name = 'forum/contact_us.html'

    def get(self, request):
        form = ContactUsForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = ContactUsForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            ContactMessage.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                message=form.cleaned_data['message']
            )
            # Display a success message
            return render(request, self.template_name, {'form': ContactUsForm(), 'success': True})
        return render(request, self.template_name, {'form': form})

class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'forum/post_detail.html'
    context_object_name = 'post'

    def get_object(self):
        return get_object_or_404(Post, slug=self.kwargs['slug'])