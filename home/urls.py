from django.urls import path
from . import views  # Ensure views.py exists in the same directory

urlpatterns = [
    path('', views.home, name='home'),  
    path('edit/<int:id>/', views.update_user, name='update_user'),  
    path('delete/<int:id>/', views.delete_user, name='delete_user'),  
]



