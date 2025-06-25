from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import LoginForm
from django.http import HttpResponseForbidden

from .models import Feedback, User
from .forms import FeedbackForm

from .models import Feedback as FeedbackModel
from django.shortcuts import get_object_or_404
from django.contrib import messages

from collections import defaultdict
from django.utils.timezone import localtime

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = LoginForm()
    return render(request, 'feedback/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard(request):
    return render(request, 'feedback/dashboard.html')

@login_required
def home(request):
    return render(request, 'feedback/home.html')


from collections import defaultdict

@login_required
def dashboard(request):
    user = request.user

    if user.role == 'manager':
        feedbacks = Feedback.objects.filter(created_by=user).select_related('created_for')
        
        # Count feedbacks received per employee
        feedback_counts = defaultdict(int)
        for fb in Feedback.objects.filter(created_by=user):
            feedback_counts[fb.created_for.id] += 1

        return render(request, 'feedback/dashboard.html', {
            'feedbacks': feedbacks,
            'feedback_counts': dict(feedback_counts),
        })
    
    elif user.role == 'employee':
        feedbacks = Feedback.objects.filter(created_for=user).order_by('-created_at')
        return render(request, 'feedback/dashboard.html', {'feedbacks': feedbacks})


@login_required
def assign_feedback(request):
    if request.user.role != 'manager':
        return redirect('dashboard')
    
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.created_by = request.user
            feedback.save()
            return redirect('dashboard')
    else:
        form = FeedbackForm()
    
    return render(request, 'feedback/assign_feedback.html', {'form': form})

@login_required
def view_feedback(request):
    if request.user.role == 'manager':
        # Get feedbacks given by the manager and optimize fetching the related employee
        feedbacks = Feedback.objects.filter(created_by=request.user)
    else:
        # Get feedbacks received by the employee
        feedbacks = Feedback.objects.filter(created_for=request.user)

        # Handle employee comment submission
        if request.method == 'POST':
            feedback_id = request.POST.get('feedback_id')
            comment = request.POST.get('employee_comment')
            feedback = get_object_or_404(Feedback, id=feedback_id, created_for=request.user)
            feedback.employee_comment = comment
            feedback.save()
            messages.success(request, "Your comment has been saved.")
            return redirect('view_feedback')

    return render(request, 'feedback/view_feedback.html', {'feedbacks': feedbacks})


@login_required
def acknowledge_feedback(request, pk):
    feedback = get_object_or_404(Feedback, pk=pk, created_for=request.user)
    feedback.acknowledged = True
    feedback.save()
    return redirect('view_feedback')

@login_required
def edit_feedback(request, pk):
    feedback = get_object_or_404(Feedback, pk=pk, created_by=request.user)

    if request.method == 'POST':
        form = FeedbackForm(request.POST, instance=feedback)
        if form.is_valid():
            form.save()
            messages.success(request, "Feedback updated successfully.")
            return redirect('view_feedback')
        else:
            messages.error(request, "Invalid form submission.")
    else:
        form = FeedbackForm(instance=feedback)

    return render(request, 'feedback/edit_feedback.html', {'form': form})

@login_required
def delete_feedback(request, pk):
    feedback = get_object_or_404(Feedback, pk=pk, created_by=request.user)

    if request.method == 'POST':
        feedback.delete()
        messages.success(request, "Feedback deleted successfully.")
        return redirect('view_feedback')

    return render(request, 'feedback/delete_confirm.html', {'feedback': feedback})


 
