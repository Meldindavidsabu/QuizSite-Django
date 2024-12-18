from django.contrib.auth.models import User
from django.db import models

class Quiz(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)  

    def __str__(self):
        return self.name

class Question(models.Model):
    question_text = models.CharField(max_length=255)
    option_a = models.CharField(max_length=100)
    option_b = models.CharField(max_length=100)
    option_c = models.CharField(max_length=100)
    option_d = models.CharField(max_length=100)
    correct_option = models.CharField(max_length=1, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')])
    category = models.CharField(max_length=100)  
    
    quiz = models.ForeignKey(Quiz, related_name="questions", on_delete=models.CASCADE, null=True, blank=True)  

    def __str__(self):
        return self.question_text

class Submission(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_answer = models.CharField(max_length=1, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')])
    is_correct = models.BooleanField()

    def __str__(self):
        return f"{self.user.username} - Question: {self.question.id}, Correct: {self.is_correct}"

class UserQuiz(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    score = models.FloatField()
    date_attended = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.user.username} - {self.quiz.name}'
