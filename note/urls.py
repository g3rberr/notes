from django.urls import path
from .views import *


app_name = 'notes'

urlpatterns = [
    path('view_note/', view_note, name='view_note'),
    path('add_note/', add_note, name='add_note'),
    path('edit_note/', edit_note, name='edit_note'),
    path('delete_note/', delete_note, name='delete_note'),

    path('tags/', all_tags, name='tags'),
    path('view_tag/', view_tag, name='view_tag'),
    path('add_tag/', add_tag, name='add_tag'),
    path('delete_tag/', delete_tag, name='delete_tag')
]
