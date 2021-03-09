from django.urls import path
from .views import SignUp , Login  , Logout

app_name = 'accounts'
urlpatterns = [
    path('signup/',SignUp, name = 'signup'),
    path('login/',Login, name = 'login'),
    path('logout/',Logout, name = 'logout'),
]