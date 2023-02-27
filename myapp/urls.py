from django.urls import path
from . import views
import myapp
app_name = 'myapp'

urlpatterns = [
    path('/', views.index, name='index'),
    path('/profile', views.profile_view, name='profile'),
    path('/home', views.home_view, name='home'),
    path('/quiz', views.quiz_view, name='quiz'),
    path('/contest', views.contest_view, name='contest'),
    path('/logout', views.logout_view, name='logout')
]