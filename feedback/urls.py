from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('assign-feedback/', views.assign_feedback, name='assign_feedback'),
    path('view-feedback/', views.view_feedback, name='view_feedback'),
    path('feedback/<int:pk>/acknowledge/', views.acknowledge_feedback, name='acknowledge_feedback'),
    path('delete-feedback/<int:feedback_id>/', views.delete_feedback, name='delete_feedback'),
    path('feedback/<int:pk>/edit/', views.edit_feedback, name='edit_feedback'),
    path('feedback/<int:pk>/delete/', views.delete_feedback, name='delete_feedback'),
]