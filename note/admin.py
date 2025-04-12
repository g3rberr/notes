from django.contrib import admin

from .models import Tag, Note

admin.site.register(Tag)


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    fields = (('title', 'content'), 'user', 'tags', ('added_on', 'updated_on'))
    readonly_fields = ('added_on', 'updated_on')