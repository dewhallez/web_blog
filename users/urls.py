"""Define URL patters for users"""
from django.urls import path, include



from . import views

app_name = 'users'

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    # Registration page.
    path('register/', views.register, name='register'),
    # Login Page
    #path('login/', login, {'template_name': 'registrations/login.html'}, name='login'),

]