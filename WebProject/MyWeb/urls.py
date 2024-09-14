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
    path('beginner_questions/', views.beginner_questions, name='beginner_questions'),
    path('intermidiate_questions/', views.intermidiate_questions, name='intermidiate_questions'),
    path('professional_questions/', views.professional_questions, name='professional_questions'),
    path('expert_questions/', views.expert_questions, name='expert_questions'),
    path('projects_ideas/', views.projects_ideas, name='projects_ideas'),
]
