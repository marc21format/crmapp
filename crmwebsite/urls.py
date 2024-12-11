from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views  

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('instructor_roster/', views.instructor_roster, name='instructor_roster'),  
    path('instructor/<int:pk>/', views.instructor_details, name='instructor'),  
    path('delete_instructor/<int:pk>/', views.delete_instructor, name='delete_instructor'),  
    path('update_instructor/<int:pk>/', views.update_instructor, name='update_instructor'),  
    path('add_instructor/', views.add_instructor, name='add_instructor'), 
    path('instructor/<int:pk>/confirm_delete/', views.confirm_delete_instructor, name='confirm_delete_instructor'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #profile picture pero static at pang localhost lang       