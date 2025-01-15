from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.views import View
from .models import Bio

def mybio(request):
    bio = Bio.objects.all()
    return render(request, 'comet/comet.html', {'bio': bio})

class UserProfileView(View):
    template_name = 'comet/comet.html'

    def get(self, request, username):
        user = get_object_or_404(User, username=username)
        return render(request, self.template_name, {'profile_user': user})