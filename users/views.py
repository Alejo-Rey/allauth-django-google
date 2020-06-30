from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .models import CustomUser, Education

from .forms import CustomUserCreationForm, EducationForm

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'



class EducationView(CreateView):
    model = Education
    form_class = EducationForm
    template_name = "add_education.html"
    success_url = 'education'

def add_education(request):
    """ Adds information about education """
    user = request.user

    if request.method == 'POST':
        form = EducationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            e = Education(
                user=user,
                school=data['school'],
                degree=data['degree'],
                start_year=data['start_year'],
                end_year=data['end_year'],
                description=data['description']
            )
            e.save()
            response = HttpResponse(status=302)
            response['Location'] = 'profile#education'
            return response
    else:
        form = EducationForm()

    return render(
        request=request,
        template_name='add_education.html',
        context={'form': form}
    )