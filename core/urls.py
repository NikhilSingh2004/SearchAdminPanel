from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import HomeView, UserSignUpView, UserLoginView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('signup/', UserSignUpView.as_view(), name='signup'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
]
