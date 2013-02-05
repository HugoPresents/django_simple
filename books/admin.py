from django.contrib import admin
from books.models import Publisher, Author, Book

# define customize list style
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email')

class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'publication_date', 'publisher')
    # use this line to support filter results
    # don't forget "," end of the line!
    list_filter = ('publication_date',)
    # I'm not fully understand here~
    date_hierarchy = 'publication_date'
admin.site.register(Publisher)
# register customize class
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)