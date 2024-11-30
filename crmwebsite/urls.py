from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views  # Your views here

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('instructor_roster/', views.instructor_roster, name='instructor_roster'),  # Instructor roster page
    path('instructor/<int:pk>/', views.instructor_details, name='instructor'),  # Instructor details page
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)