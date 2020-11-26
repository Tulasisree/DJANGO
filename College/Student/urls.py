from django.urls import path
from Student import views

urlpatterns = [
    path('register/',views.register,name='register'),
    path('show/',views.show,name='student_data'),
    path('edit/<int:num>',views.update,name='student_update'),
    path('delete/<int:num>',views.delete,name='student_delete'),
    path('addBook/',views.add_book,name='add_book'),
    path('editBook/<int:id>',views.edit_book,name='edit_book'),
    path('books/',views.books,name='books'),
    path('details/<str:branch>',views.details,name='details')
]