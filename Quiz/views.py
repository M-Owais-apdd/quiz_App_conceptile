from django.shortcuts import render
from .models import Question,QuizSession
import random
# Create your views here.

def index(request):
    return render(request,'index.html')

def start_quiz(request):
    session, created = QuizSession.objects.get_or_create(id=1) 
    session.total_questions = 0
    session.correct_answers = 0
    session.incorrect_answers = 0
    session.save()
    return render(request, 'start_quiz.html', {"message": "New quiz session started."})

def get_question(request):
    questions = list(Question.objects.all())
    if not questions:
        return render(request, 'error.html', {"error": "No questions available."})

    question = random.choice(questions)
    question_data = {
        "id": question.id,
        "text": question.text,
        "options": {
            "A": question.option_a,
            "B": question.option_b,
            "C": question.option_c,
            "D": question.option_d,
        },
    }
    return render(request, 'question.html', question_data)

def submit_answer(request):
    if request.method == "POST":
        question_id = request.POST.get("question_id")
        selected_option = request.POST.get("selected_option")

        try:
            question = Question.objects.get(id=question_id)
            session = QuizSession.objects.get(id=1)
        except (Question.DoesNotExist, QuizSession.DoesNotExist):
            return render(request, 'error.html', {"error": "Invalid question or session."})

        session.total_questions += 1
        if selected_option == question.correct_option:
            session.correct_answers += 1
            result = "correct"
        else:
            session.incorrect_answers += 1
            result = "incorrect"

        session.save()
        return render(request, 'answer.html', {"result": result})

    return render(request, 'error.html', {"error": "Invalid request method."})

def quiz_summary(request):
    try:
        session = QuizSession.objects.get(id=1)
    except QuizSession.DoesNotExist:
        return render(request, 'error.html', {"error": "No quiz session found."})

    summary = {
        "total_questions": session.total_questions,
        "correct_answers": session.correct_answers,
        "incorrect_answers": session.incorrect_answers,
    }
    return render(request, 'summary.html', summary)