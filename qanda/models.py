from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.contrib import auth

# Create your models here.

class User(auth.models.User,auth.models.PermissionsMixin):

    def __str__(self):
        return self.username




class Question(models.Model):
    author = models.ForeignKey('auth.user',on_delete=models.CASCADE)
    asked_date = models.DateTimeField(default=timezone.now())
    asked_ques = models.TextField()
    topic_related = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    upload = models.ImageField(upload_to='folder',blank=True)

    def __str__(self):
        return self.asked_ques

    def save(self,*args,**kwargs):
        varib = self.asked_ques[:25]
        self.slug = slugify(varib)
        super(Question,self).save(*args,**kwargs)


    def get_absolute_url(self):
        return reverse('question_detailview',kwargs={'slug':self.slug})


class Answer(models.Model):
    question = models.ForeignKey('qanda.Question',related_name='answer',on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    ques_ans = models.TextField()
    ans_date = models.DateTimeField(default=timezone.now())
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.ques_ans

    def save(self,*args,**kwargs):
        varib = self.ques_ans[:25]
        self.slug = slugify(varib)
        super(Answer,self).save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse('question_detailview',kwargs={'slug':self.slug})
