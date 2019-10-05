from django.contrib.auth import authenticate, get_user_model, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from rest_framework import viewsets

from .forms import CustomUserCreationForm
from .serializers import UserSerializer


User = get_user_model()


def signup(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()

    return render(request, 'user/signup.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name', '')
        if first_name:
            request.user.first_name = first_name

        last_name = request.POST.get('last_name', '')
        if last_name:
            request.user.last_name = last_name

        email = request.POST.get('email', '')
        if email:
            request.user.email = email

        request.user.save()

    return render(request, 'user/edit_profile.html')


class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer
