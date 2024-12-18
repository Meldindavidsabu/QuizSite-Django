from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Question, Submission, Quiz, UserQuiz
import random
from django.db.models import Count

def login_view(request):
  
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('quiz:start_quiz') 
            else:
                
                form.add_error(None, "Invalid username or password")
    else:
        form = AuthenticationForm()

    return render(request, 'quiz/login.html', {'form': form})

def home(request):
    return render(request, 'quiz/start.html')

def register(request):
    """Handles user registration."""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('quiz:login')
    else:
        form = UserCreationForm()
    return render(request, 'quiz/register.html', {'form': form})

@login_required
def start_quiz(request):
   
    Submission.objects.filter(user=request.user).delete()

    categories = Question.objects.values_list('category', flat=True).distinct()

    if 'category' not in request.session:
        request.session['category'] = categories[0] if categories else None
    selected_category = request.GET.get('category')
    if selected_category and selected_category in categories:
        request.session['category'] = selected_category
        return redirect('quiz:get_question')  

    return render(request, 'quiz/start.html', {'categories': categories})
@login_required
def get_question(request):
  
    if 'category' not in request.session:
        category = request.GET.get('category')
        if category:
            request.session['category'] = category
        else:
            return redirect('quiz:start_quiz')

    category = request.session['category']

    answered_questions = Submission.objects.filter(user=request.user).values_list('question_id', flat=True)

    questions = Question.objects.filter(category=category).exclude(id__in=answered_questions)
    if not questions.exists():
        return redirect('quiz:quiz_results')
    question = random.choice(questions)
    total_questions = Question.objects.filter(category=category).count()
    answered_count = answered_questions.count()
    
    progress = answered_count + 1

    return render(request, 'quiz/question.html', {
        'question': question,
        'answered_count': answered_count,
        'total_questions': total_questions,
        'progress': progress  
    })

@login_required
def submit_answer(request, question_id):
    """
    Handles answer submission, validates it, and stores the result.
    """
    if request.method == 'POST':
        user_answer = request.POST.get('user_answer')
        question = Question.objects.get(id=question_id)
        is_correct = user_answer == question.correct_option

        
        Submission.objects.create(
            question=question,
            user=request.user,
            user_answer=user_answer,
            is_correct=is_correct
        )


        return redirect('quiz:get_question')

@login_required
def quiz_results(request):
   
    submissions = Submission.objects.filter(user=request.user)
    
    if not submissions:
        
        return render(request, 'quiz/result.html', {'message': 'No submissions found for your quiz attempt.'})
    
    total_questions = submissions.count()
    correct_answers = submissions.filter(is_correct=True).count()
    incorrect_answers = total_questions - correct_answers
    percentage = (correct_answers / total_questions) * 100 if total_questions > 0 else 0
    if correct_answers == 0:
        message = f"Sorry {request.user.username}, unfortunately, all your answers are wrong and you scored 0%."
    else:
        message = f"Congratulations {request.user.username}! You scored {percentage:.2f}%."

    first_submission = submissions.first()
    quiz = first_submission.question.quiz if first_submission else None
    
    context = {
        'total_questions': total_questions,
        'correct_answers': correct_answers,
        'incorrect_answers': incorrect_answers,
        'percentage': percentage,
        'submissions': submissions,
        'message': message
    }

    return render(request, 'quiz/result.html', context)

