from django import forms
from .models import Question, Answer

class QuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ['title', 'content',]
        labels = {
            'title': '제목',
            'content': '내용',
        }
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': '제목을 입력해주세요.'}),
            'content': forms.Textarea(attrs={'placeholder': '내용을 입력해주세요.'}),
        }

class AnswerForm(forms.ModelForm):

    class Meta:
        model = Answer
        fields = ['content',]
        labels = {
            'content': '',
        }
        widgets = {
            'content': forms.TextInput(attrs={'placeholder': '답글을 입력해주세요.', 'style': 'width:400px;'}),
        }