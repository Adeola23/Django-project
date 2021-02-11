from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import ScrumyGoals ,GoalStatus
from django.contrib.auth.models import User
import random


def index(request):
    goal = ScrumyGoals.objects.filter(goal_name = 'Learn Django')
    return HttpResponse (goal)

def move_goal(request, **kwargs):
    output = ScrumyGoals.objects.get(goal_id = kwargs['goal_id'])
    return HttpResponse (output)
    
def add_goal(request):
    first = ScrumyGoals.objects.create(goal_name = 'Keep learning Django', goal_id= random.randrange(1000,9999,2) , created_by= 'louis', moved_by='louis', owner= 'louis', goal_status= GoalStatus.objects.get(status_name = 'Weekly Goal'), user=User.objects.get(username = 'louis'))
    first.save()
    return HttpResponse (first)
    #return HttpResponse('This is a Scrum Application')
# Create your views here.

def home(request):
    add = ScrumyGoals.objects.all()
    add = ScrumyGoals.objects.filter(goal_name = 'Keep learning Django')
    output = ', '.join([eachgoal.goal_name for eachgoal in add])
    return HttpResponse(output)

