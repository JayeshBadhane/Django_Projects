from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Home page
    path('contactData/', views.contactData, name='contactData'),  # Contact Data page
    
    # Add other URL patterns here
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
