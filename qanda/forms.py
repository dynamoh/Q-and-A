from django import forms
from django.contrib.auth import get_user_model
from .models import Question,Answer
from django.contrib.auth.forms import UserCreationForm

class QuestionForm(forms.ModelForm):
    class Meta():
        model = Question
        fields =('author','topic_related','asked_ques','upload')

class AnswerForm(forms.ModelForm):
    class Meta():
        model = Answer
        fields =('author','ques_ans')

class UserCreateForm(UserCreationForm):

    class Meta:
        fields = ('username','email','password1','password2')
        model = get_user_model()

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['username'].label = 'Display Name'
        self.fields['email'].label = 'Email Address'
        self.fields['password1'].label = 'Password'
        self.fields['password2'].label = 'Confirm Password'
