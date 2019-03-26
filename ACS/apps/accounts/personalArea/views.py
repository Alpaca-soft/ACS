from django.conf import settings
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required


def view_profile(request, pk=None):
    if pk:
        try:
            user = User.objects.get(pk=pk)  # Профиль пользователя
        except User.DoesNotExist:
            user = ''
    else:
        user = request.user  # Свой профиль
    context = {
        'user': user,
    }
    return render(request, 'accounts/profile/profile.html', context)


def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect(reverse('accounts:profile'))
    else:
        form = EditProfileForm(instance=request.user)
        context = {
            'form': form
        }
        return render(request, 'accounts/profile/edit_profile.html', context)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect(reverse('accounts:view_profile'))
        else:
            return redirect(reverse('accounts:change_password'))
    else:
        form = PasswordChangeForm(user=request.user)
        context = {
            'form': form
        }
        return render(request, 'accounts/profile/change_password.html', context)

