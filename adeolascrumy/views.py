from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import ScrumyGoals


def index(request):
    goal = ScrumyGoals.objects.filter(goal_name = 'Learn Django')
    return HttpResponse (goal)
    
    #return HttpResponse('This is a Scrum Application')
# Create your views here.
