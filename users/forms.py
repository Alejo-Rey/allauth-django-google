from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Education

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields

class EducationForm(forms.ModelForm):
    school = forms.CharField(min_length=3, max_length=50, required=True)
    degree = forms.Charschool = forms.CharField(min_length=3, max_length=50, required=True)
    start_year = forms.Charschool = forms.CharField(required=False, widget=forms.widgets.DateTimeInput(attrs={"type": "date"}))
    end_year = forms.Charschool = forms.CharField(required=False, widget=forms.widgets.DateTimeInput(attrs={"type": "date"}))
    description = forms.Charschool = forms.CharField(min_length=3, max_length=200, required=True)
    class Meta:
        model = Education
        fields = ['school','degree','start_year','end_year','description']