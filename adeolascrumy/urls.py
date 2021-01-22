from django.urls import path
from adeolascrumy import views
urlpatterns = [
    path('', views.index)
]