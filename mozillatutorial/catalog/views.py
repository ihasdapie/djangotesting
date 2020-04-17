from django.shortcuts import render
from catalog.models import *
from django.views import generic

# Create your views here.

def index(request):
    """view function for home page"""

    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    num_instances_avaliable = BookInstance.objects.filter(status__exact = 'a').count()

    num_authors = Author.objects.count()

#num of visits to this view
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1


    context = {
        'num_books' : num_books,
        'num_instances': num_instances,
        'num_authors': num_authors,
        'num_instances_avaliable':num_instances_avaliable,
        'num_visits': num_visits,
    }
    #return w/ index.html template & defined variables
    return render(request, 'index.html', context=context)

'''
class BookListView(generic.ListView):
    model = Book
    context_object_name = 'my_book_list' #name for list as template variable
    paginate_by=2
    def get_queryset(self):
        queryset=Book
#queryset = Book.objects.filter(title__icontains="1")[:5] #returns 5 books with '1' in the title
        return queryset
    def get_context_data(self, **kwargs):
#override base implementation
        context = super(BookListView, self).get_context_data(**kwargs)
        context['some_data'] = 'just some data'
        return context
'''

class BookListView(generic.ListView):
    model = Book

class BookDetailView(generic.DetailView):
    model = Book






