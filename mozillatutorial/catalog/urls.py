from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('books/<int:pk>', views.BookDetailView.as_view(), name = 'book-detail'), #use <int:pk> as a stand-in to accept the specific book id
    #<int:pk> will capture an int as a formatted string, then pass it to the view as a parameter named pk (primary key)

]
