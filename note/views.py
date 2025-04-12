from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect, JsonResponse, HttpResponseForbidden
from django.contrib.auth.decorators import login_required

from .models import Note, Tag
from .forms import AddNoteForm, AddTagForm, EditNoteForm

@login_required
def view_note(request):
    notes = Note.objects.filter(user=request.user)
    note_id = request.GET.get('note')
    note = get_object_or_404(notes, id=note_id)

    context = {'note': note}
    return render(request, 'note/view_note.html', context)


@login_required
def add_note(request):
    if request.method == 'POST':
        form = AddNoteForm(data=request.POST, user=request.user)
        if form.is_valid():
            note = form.save(commit=False)
            note
            note.user = request.user
            note.save() 
            form.save_m2m() 
            return HttpResponseRedirect(reverse('users:profile_settings'))
    else:
        form = AddNoteForm(user=request.user)
    context = {'form': form}
    return render(request, 'note/add_note.html', context)



@login_required
def edit_note(request):
    note_id = request.GET.get('note')
    note = get_object_or_404(Note, id=note_id)
    if request.method == 'POST':
        form = EditNoteForm(data=request.POST, user=request.user, instance=note)
        if form.is_valid():
            form.save()
            url = f'{reverse('notes:view_note')}?note={note_id}'
            return HttpResponseRedirect(url)
    else:
        form = EditNoteForm(instance=note, user=request.user)
    context = {'form': form,
               'note': note}
    return render(request, 'note/edit_note.html', context)


@login_required
def all_tags(request):
    tags = Tag.objects.filter(user=request.user)
    context = {'tags': tags,}
    return render(request, 'note/edit_tag.html', context)


@login_required
def view_tag(request):
    tags = Tag.objects.filter(user=request.user)
    tag_id = request.GET.get('tag')
    tag = get_object_or_404(tags, id=tag_id)
    notes = Note.objects.filter(user=request.user, tags=tag)
    context = {'tag': tag, 'notes': notes}
    return render(request, 'note/view_tag.html', context)


@login_required
def add_tag(request):
    if request.method == 'POST':
        form = AddTagForm(data=request.POST)
        if form.is_valid():
            tag = form.save(commit=False)
            tag.user = request.user
            tag.save()
            return HttpResponseRedirect(reverse('notes:tags'))
    else:
        form = AddTagForm()
    context = {'form': form}

    return render(request, 'note/add_tag.html', context)


@login_required
def delete_tag(request):
    if request.method == 'POST':
        tag_id = request.POST.get('tag') 
        tag = get_object_or_404(Tag, id=tag_id, user=request.user)  
        tag.delete()  
        return redirect('notes:tags') 
    return HttpResponseForbidden("Forbidden")  
   

@login_required
def delete_note(request):
    if request.method == 'POST':
        tag_id = request.POST.get('note')  
        tag = get_object_or_404(Note, id=tag_id, user=request.user)  
        tag.delete()  
        return redirect('notes:profile')  
    return HttpResponseForbidden("Forbidden")  
   
