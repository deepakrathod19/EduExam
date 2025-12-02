
from django.urls import path

from examapp import views

urlpatterns=[
    path('showform/',views.showForm),
    path('viewquestion/',views.viewQuestion),
    path('addquestion/',views.addQuestion),
    path('updatequestion/',views.updateQuestion),
    path('deletequestion/',views.deleteQuestion),
    path('givemeregister/',views.giveMeRegister),
    path('login/',views.login),
    path('register/', views.register),
    path('givemelogin/', views.giveMeLogin),
    path('nextquestion/',views.nextQuestion),
    path('starttest/', views.startTest),
    path('previousquestion/',views.previousQuestion),
    path('endexam/',views.endExam),
    path('senddata/',views.sendData),
    path('getuser/<uname>',views.getUser),
    path('adduser/',views.addUser),
    path('updateuser/',views.updateUser),
    path('deleteuser/<uname>',views.deleteUser),
    path('getalluser/',views.getAllUser),
    # path('getuser2/<uname>',views.getUser2)
]