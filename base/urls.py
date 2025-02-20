from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('edit-note/<str:pk>/', views.edit_note, name='edit-note'),
    path('note/<str:pk>/', views.get_note_detail, name='note-detail'),
    path('create-note/', views.create_note, name='create-note'),
]
        
if __name__ == '__main__':
    print(urlpatterns)


