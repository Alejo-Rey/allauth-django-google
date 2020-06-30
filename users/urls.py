from django.urls import path
from .views import SignUpView, EducationView, add_education

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('me/education', EducationView.as_view(), name='add_education'),
    path('me/education2', add_education, name='add_education2'),
]