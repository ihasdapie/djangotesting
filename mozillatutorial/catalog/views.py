from django.shortcuts import render

# Create your views here.

from catalog.models import *

def index(request):
    """view function for home page"""

    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    num_instances_avaliable = BookInstance.objects.filter(status__exact = 'a').count()

    num_authors = Author.objects.count()

    context = {
        'num_books' : num_books,
        'num_instances': num_instances,
        'num_authors': num_authors.
        'num_instances_avaliable':num_instances_avaliable,
    }
    #return w/ index.html template & defined variables
    return render(request, 'index.html', context=context)



