
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),  
    path('quiz/', include('quiz.urls')),  
    path('accounts/', include('django.contrib.auth.urls')),  
    path('', lambda request: redirect('quiz:register')),  
]
