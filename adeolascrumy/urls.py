from django.urls import path, include
from adeolascrumy import views
app_name = 'adeolascrumy'

urlpatterns = [
    path('', views.index, name='index'),
    path('movegoal/<int:goal_id>', views.move_goal),
    path('addgoal/', views.add_goal, name='addgoal'),
    path('home/', views.home),
    path('accounts/', include('django.contrib.auth.urls')) ,
    
    

]
 