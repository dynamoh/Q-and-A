from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import ListView,DetailView,UpdateView,DeleteView,TemplateView,CreateView
from .models import Question,Answer
from .forms import QuestionForm,AnswerForm,UserCreateForm
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.db.models import Q
# Create your views here.




class MyListView(ListView):
    model = Question

    def get_queryset(self):
        sreq = self.request.GET.get("searchrequest")
        if sreq==None:
            return Question.objects.filter(asked_date__lte=timezone.now()).order_by('-asked_date')
        else:
            return Question.objects.filter(Q(asked_ques__icontains = sreq) | Q(topic_related__icontains = sreq)).order_by('-asked_date')


class MyDetailView(DetailView):
    model = Question

class MyCreateView(LoginRequiredMixin,CreateView):
    login_url='/login/'
    redirect_field_name = 'question_detailview'
    form_class = QuestionForm
    model = Question

class MyUpdateView(LoginRequiredMixin,UpdateView):
    model = Question
    login_url='/login/'
    redirect_field_name = 'question_detailview'
    form_class = QuestionForm

class MyAboutPage(TemplateView):
    template_name='about.html'

class MyLogoutView(TemplateView):
    template_name = 'registration/logout.html'

class MyDeleteView(LoginRequiredMixin,DeleteView):
    login_url='/login/'
    success_url = reverse_lazy('question_listview')
    model = Question

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            save_it = form.save(commit=False)
            save_it.save()
            subject='Thank You for Signing up'
            message = 'gfmgfc fghv jhfv jf,cv c dgghmv cmv yhjf'
            from_email = settings.EMAIL_HOST_USER
            to_list = [save_it.email]
            send_mail(subject,message,from_email,to_list,fail_silently=True)
            username = form.cleaned_data.get('username')
            raw_password=form.cleaned_data.get('password1')
            user = authenticate(username=username,password=raw_password)
            login(request, user)
            return redirect('aboutpage')
    else:
        form=UserCreationForm()

    return render(request,'accounts/signup.html',{'form':form})


@login_required
def add_answer_to_question(request,slug):
    question = get_object_or_404(Question,slug=slug)
    if request.method =='POST':
        form =AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = question
            answer.save()
            return redirect('question_detailview',slug=question.slug)
    else:
        form=AnswerForm()
    return render(request,'answer_form.html',{'form':form})


@login_required
def remove_answer(request,slug):
    answer = get_object_or_404(Answer,slug=slug)
    post_slug = answer.question.slug
    answer.delete()
    return redirect('question_detailview',slug=post_slug)
