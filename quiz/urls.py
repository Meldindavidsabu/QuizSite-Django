from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

app_name = 'quiz'  

urlpatterns = [
    path('', views.home, name='home'),  
    path('register/', views.register, name='register'),  
    path('login/', views.login_view, name='login'),  
    path('start/', views.start_quiz, name='start_quiz'),  

    
    path('question/', views.get_question, name='get_question'),  
    path('question/<int:question_id>/', views.get_question, name='get_question_by_id'),  
    path('submit_answer/<int:question_id>/', views.submit_answer, name='submit_answer'),

    path('submit_answer/<int:question_id>/', views.submit_answer, name='submit_answer'),  
    path('results/', views.quiz_results, name='quiz_results'),  
    path('logout/', LogoutView.as_view(), name='logout'), 
    
]
