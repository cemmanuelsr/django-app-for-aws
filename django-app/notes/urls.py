from django.urls import path

from . import views

urlpatterns = [
    path('notes/', views.get_notes),
    path('notes/<int:note_id>', views.get_note),
    path('notes/create/', views.create_note),
    path('notes/delete/<int:note_id>', views.delete_note),
    path('notes/update/<int:note_id>', views.update_note)
]
