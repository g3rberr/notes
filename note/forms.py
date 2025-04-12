from django import forms
from django.shortcuts import get_list_or_404

from users.models import User
from note.models import Note, Tag


class AddNoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content', 'tags']  
        widgets = {
            'title': forms.Textarea(attrs={'class': 'form-control dark-input'})
        }        

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
    
        self.fields['tags'].queryset = Tag.objects.filter(user=self.user)


    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.none(),
        widget=forms.SelectMultiple(attrs={'class': 'tag form-control dark-input'}),
        required=False
    )

    content = forms.CharField(
        label="Content",
        widget=forms.Textarea(attrs={
            'class': 'form-control dark-input',
            'rows': 20,
            'cols': 90,
            'placeholder': 'Write your note here'
        })
    )


class EditNoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content', 'tags']  
        widgets = {
            'title': forms.Textarea(attrs={'class': 'form-control dark-input'})
        }        

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
    
        self.fields['tags'].queryset = Tag.objects.filter(user=self.user)


    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.none(),
        widget=forms.SelectMultiple(attrs={'class': 'tag form-control dark-input'}),
        required=False
    )

    content = forms.CharField(
        label="Content",
        widget=forms.Textarea(attrs={
            'class': 'form-control dark-input',
            'rows': 20,
            'cols': 90,
            'placeholder': 'Write your note here'
        })
    )



class AddTagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ('name',)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control dark-input no_borders'})
        }

