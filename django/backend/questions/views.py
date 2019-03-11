from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import redirect
from .models import Question
from .forms import QuestionForm


class IndexView(ListView):

    model = Question
    template_name = 'index.html'

    def get_queryset(self):
        return Question.objects.order_by('-id')


class AskView(CreateView):

    model = Question
    form_class = QuestionForm
    template_name = 'ask.html'
