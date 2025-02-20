from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('edit-note/<str:pk>/', views.edit_note, name='edit-note'),

]
        
if __name__ == '__main__':
    print(urlpatterns)


