from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import ScrumyGoals ,GoalStatus
from django.contrib.auth.models import User
import random


def index(request):
    goal = ScrumyGoals.objects.filter(goal_name = 'Learn Django')
    return HttpResponse (goal)

def move_goal(request, **kwargs):


    try: 
	    obj = ScrumyGoals.objects.get(goal_id=kwargs['goal_id'])

    except Exception as e: 
        return render(request, 'adeolascrumy/exception.html', {'error' : 'A record with that goal id does not exist'}) 
    else: 
	    return HttpResponse(obj.goal_name) 
    
    
def add_goal(request):
    first = ScrumyGoals.objects.create(goal_name = 'Keep learning Django', goal_id= random.randrange(1000,9999,2) , created_by= 'louis', moved_by='louis', owner= 'louis', goal_status= GoalStatus.objects.get(status_name = 'Weekly Goal'), user=User.objects.get(username = 'louis'))
    first.save()
    return HttpResponse (first)
    #return HttpResponse('This is a Scrum Application')
# Create your views here.

def home(request):
    data_query = {}
    users = User.objects.all()
    weekly_goals = ScrumyGoals.objects.filter(goal_status=GoalStatus.objects.get(status_name='Weekly Goal'))
    daily_goals = ScrumyGoals.objects.filter(goal_status=GoalStatus.objects.get(status_name='Daily Goal'))
    verify_goals = ScrumyGoals.objects.filter(goal_status=GoalStatus.objects.get(status_name='Verify Goal'))
    done_goals = ScrumyGoals.objects.filter(goal_status=GoalStatus.objects.get(status_name='Done Goal'))
    data_query['users'] = users
    data_query['weekly_goals'] = weekly_goals
    data_query['daily_goals'] = daily_goals
    data_query['verify_goals'] = verify_goals
    data_query['done_goals'] = done_goals
    return render(request, 'adeolascrumy/home.html', data_query)



    #data_query['goal_id'] = form.goal_id
    #data_query['user'] = form.user
    ##return render(request, 'adeolascrumy/home.html', data_query)
    

    #add = ScrumyGoals.objects.all()
    #add = ScrumyGoals.objects.filter(goal_name = 'Keep learning Django')
    #output = ', '.join([eachgoal.goal_name for eachgoal in add])
    #return HttpResponse(output)

