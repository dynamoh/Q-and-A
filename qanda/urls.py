from django.contrib import admin
from django.urls import path,include
from .views import MyUpdateView,MyListView,MyAboutPage,MyCreateView,MyDeleteView,MyDetailView,MyLogoutView,signup,add_answer_to_question,remove_answer
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('list/',MyListView.as_view(),name="question_listview"),
    path('detail/<str:slug>/',MyDetailView.as_view(),name="question_detailview"),
    path('update/<str:slug>/',MyUpdateView.as_view(),name="question_updateview"),
    path('delete/<str:slug>/',MyDeleteView.as_view(),name="question_deleteview"),
    path('create/',MyCreateView.as_view(),name="question_createview"),
    path('',MyAboutPage.as_view(),name='aboutpage'),
    path('logout/',MyLogoutView.as_view(),name='logoutpage'),
    path('signup/',signup,name='signupview'),
    path('detail/<str:slug>/answer/',add_answer_to_question,name='add_answer'),
    path('answer/<str:slug>/remove/',remove_answer,name='remove_answer'),
]

if settings.DEBUG :
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
