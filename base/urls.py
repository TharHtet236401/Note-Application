from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

]
        
if __name__ == '__main__':
    print(urlpatterns)


