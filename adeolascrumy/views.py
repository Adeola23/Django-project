from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import ScrumyGoals


def index(request):
    goal = ScrumyGoals.objects.filter(goal_name = 'Learn Django')
    return HttpResponse (goal)

def move_goal(request, **kwargs):
    output = ScrumyGoals.objects.get(goal_id = kwargs['goal_id'])
    return HttpResponse (output)
    
    #return HttpResponse('This is a Scrum Application')
# Create your views here.
