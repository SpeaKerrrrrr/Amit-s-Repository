from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('profile/', views.profile, name='profile'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('about/', views.about, name='about'), 
    path('start-learning/', views.start_learning, name='start_learning'),
    path('beginner/', views.beginner, name='beginner'),
    path('intermediate/', views.intermediate, name='intermediate'),
    path('professional/', views.professional, name='professional'),
    path('expert/', views.expert, name='expert'),
    path('beginner/questions/', views.beginner_questions, name='beginner_questions'),
    path('check_answer/', views.check_answer, name='check_answer'),
    path('beginner/questions/2/', views.beginner_question_2, name='beginner_question_2'),
    path('check_answer_2/<str:answer>/', views.check_answer_2, name='check_answer_2'),
]