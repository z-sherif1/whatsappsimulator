from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .forms import ProfileForm,RegisterForm
from .models import Profile
# Create your views here.
# register
def register_view(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password1 = form.cleaned_data['password1']

            User.objects.create_user(
                username=username,
                email=email,
                password=password1
            )
            return redirect('login')
    else:
        form = RegisterForm()
    context = {'form':form}
    return render(request ,'accounts/register.html', context )

# profile
@login_required
def profile_view(request):
    profile = request.user.profile
    context ={'profile':profile}
    return render(request, 'accounts/profile.html', context)

# profile update
@login_required
def profile_update_view(request):
    profile = request.user.profile
    if request.method=='POST':
        form = ProfileForm(request.POST, request.FILES ,instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)

    context ={'form':form}
    return render(request, 'accounts/profile_update.html', context)


