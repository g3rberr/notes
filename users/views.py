from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages



from note.models import Note, Tag
from .forms import LoginForm, SignUpForm, ChangeEmailForm, ChangePasswordForm


def loginview(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse('main:homepage'))
            else:
                messages.error(request, f"Incorrect password or username")
    else:
        form = LoginForm()
    context = {'form': form}
    return render(request, 'users/login.html', context)


def signupview(request):
    if request.method == 'POST':
        form = SignUpForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You signup succesfully')
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = SignUpForm()
    context = {'form': form}
    return render(request, 'users/signup.html', context) 


@login_required
def logoutview(request):
    logout(request)
    return HttpResponseRedirect(reverse('main:homepage'))


@login_required
def profile(request):
    notes = Note.objects.filter(user=request.user).order_by('-added_on')
    tags = Tag.objects.filter(user=request.user)
    context = {'notes': notes, 'tags': tags}

    return render(request, 'users/profile.html', context)

@login_required
def profile_search_notes(request):
    query = request.GET.get('q', '')  
    if query:
        notes = Note.objects.filter(title__icontains=query)
    else:

        notes = Note.objects.filter(user=request.user).order_by('-added_on')

    context = {
        'notes': notes
    }
    
    html = render_to_string('users/partials/search_result.html', context)
    
    return JsonResponse({'html': html})



@login_required
def profile_settings(request):
    return render(request, 'users/profile_settings.html')    


def profile_settings_search_notes(request):
    query = request.GET.get("q", "")
    results = []

    if query:
        notes = Note.objects.filter(title__icontains=query)[:5]
        results = [{'id': note.id, 'title': note.title} for note in notes]

    return JsonResponse({'results': results})




@login_required
def change_email(request):
    if request.method == 'POST':
        form = ChangeEmailForm(request.POST, instance=request.user, user=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:profile_settings'))

    else:
        form = ChangeEmailForm(instance=request.user, user=request.user)
    context = {'form': form}
    return render(request, 'users/change_email.html', context)


@login_required
def change_password(request):
    if request.method == 'POST':
        form = ChangePasswordForm(data=request.POST, user=request.user)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return HttpResponseRedirect(reverse('users:profile_settings'))
    else:
        form = ChangePasswordForm(user=request.user)
    return render(request, 'users/change_password.html', {'form': form})


