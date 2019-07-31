from django.contrib import admin
from .models import Question,Answer
from django.contrib.admin.options import ModelAdmin
# Register your models here.

class QuestionAdmin(ModelAdmin):
    list_display =["author","topic_related","asked_date"]
    search_fields = ["topic_related","asked_ques"]
    list_filter = ["topic_related","asked_date"]

class AnswerAdmin(ModelAdmin):
    list_display =["author","ans_date"]
    search_fields = ["ques_ans"]
    list_filter = ["ans_date"]


admin.site.register(Question,QuestionAdmin)
admin.site.register(Answer,AnswerAdmin)
