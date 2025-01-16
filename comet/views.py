import cloudinary
import cloudinary.uploader
import cloudinary.api
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.views import View
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .forms import ProfilePictureForm
from .models import Bio, UserProfile

def mybio(request):
    bio = Bio.objects.all()
    return render(request, 'comet/comet.html', {'bio': bio})

class UserProfileView(View):
    template_name = 'comet/comet.html'

    def get(self, request, username):
        user = get_object_or_404(User, username=username)
        return render(request, self.template_name, {'profile_user': user})

@login_required
def profile(request):
    # Ensure the UserProfile exists
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        profile_picture_url = request.POST.get('profile_picture')
        if profile_picture_url:
            user_profile.profile_picture = profile_picture_url
            user_profile.save()
            return JsonResponse({'status': 'success'})
    return render(request, 'comet/profile.html')