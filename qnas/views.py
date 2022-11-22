from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Question, Answer
from .forms import QuestionForm, AnswerForm
from products.models import Product
from accounts.models import User


# Create your views here.

def question_create(request, pk):
    if request.user.is_authenticated:
        product = Product.objects.get(pk=pk)
        if request.method == 'POST':
            question_form = QuestionForm(request.POST)
            if question_form.is_valid():
                question = question_form.save(commit=False)
                question.product = product
                question.user = request.user
                question_form.save()
                return redirect('products:detail', pk)
        # else:
        #     question_form = QuestionForm()
        # context = {
        #     'question_form' : question_form,
        # }
        return redirect('products:detail', pk)


def question_update(request, pk):
    question = Question.objects.get(pk=pk)
    if request.method == 'POST':
        question_update_form = QuestionForm(request.POST, instance=question)
        if question_update_form.is_valid():
            question.save()
            return redirect(request.GET.get('next'))
    else:
        question_update_form = QuestionForm(instance=question)
    context = {
        'question_update_form' : question_update_form
    }
    return render(request, 'qnas/form.html', context)

def question_delete(request, pk):
    Question.objects.get(pk=pk).delete()
    return redirect(request.GET.get('next'))

def answer_create(request, pk):
    if request.method == 'POST':
        if request.user.is_authenticated:
            question = get_object_or_404(Question, pk=pk)
            answer_form = AnswerForm(request.POST)
            if answer_form.is_valid():
                answer = answer_form.save(commit=False)
                answer.question = question
                answer.user = request.user
                answer.save()
                question.is_answered = 1
                question.save()
    return redirect(request.GET.get('next'))

def answer_update(request, pk):
    answer = Answer.objects.get(pk=pk)
    if request.method == 'POST':
        answer_update_form = AnswerForm(request.POST, instance=answer)
        if answer_update_form.is_valid():
            answer.save()
            return redirect(request.GET.get('next'))
    else:
        answer_update_form = AnswerForm(instance=answer)
    context = {
        'answer_update_form' : answer_update_form
    }
    return render(request, 'qnas/answerform.html', context)

def answer_delete(request, pk):
    if request.method == 'POST':
        Answer.objects.get(pk=pk).delete()
    return redirect(request.GET.get('next'))