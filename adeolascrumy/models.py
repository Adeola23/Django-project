from django.db import models
from django.contrib.auth.models import User



class GoalStatus(models.Model):
    status_name = models.CharField(max_length=180)

    def __str__(self):
        return self.status_name

class ScrumyGoals(models.Model):
    goal_name = models.CharField(max_length=180)
    goal_id = models.IntegerField()
    created_by = models.CharField(max_length=180)
    moved_by = models.CharField(max_length=180)
    owner = models.CharField(max_length=180)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    goal_status = models.ForeignKey(GoalStatus , on_delete=models.PROTECT)

    def __str__(self):
        return self.goal_name

class ScrumyHistory(models.Model):
    moved_by = models.CharField(max_length=180)
    created_by = models.CharField(max_length=180)
    moved_from = models.CharField(max_length=180)
    moved_to = models.CharField(max_length=180)
    time_of_action = models.DateTimeField(auto_now_add=True)
    goal = models.ForeignKey(ScrumyGoals , on_delete=models.PROTECT)

    def __str__(self):
        return self.created_by


   

    
