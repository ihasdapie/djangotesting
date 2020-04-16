from django.contrib import admin
from .models import Author, Genre, Book, BookInstance

# Register your models here.


"""
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Book)
admin.site.register(BookInstance)
"""

class AuthorAdmin(admin.ModelAdmin):
    fields=['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
admin.site.register(Author, AuthorAdmin)


class GenreAdmin(admin.ModelAdmin):
    pass
admin.site.register(Genre, GenreAdmin)



class BookInstanceInline(admin.TabularInline):
    model = BookInstance


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines=[BookInstanceInline]


#admin.site.register(Book, BookAdmin)

#can use @admin.register decorator to register instead
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availabity', {
            'fields': ('status', 'due_back')
        }),

    )

#admin.site.register(BookInstance, BookInstanceAdmin)


