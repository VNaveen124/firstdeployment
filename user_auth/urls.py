from django.urls import path
from . import views
import user_auth
app_name = 'user_auth'
urlpatterns = [
    path("/", views.index, name="index"),
    path('/login', views.login_view, name='login'),
    path('/signup', views.signup, name='signup')

]