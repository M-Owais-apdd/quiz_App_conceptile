from django.contrib import admin
from .models import QuizSession,Question
# Register your models here.
admin.site.register(Question)
admin.site.register(QuizSession)