from django import forms
from ckeditor.fields import RichTextFormField

class PersonalInfoForm(forms.Form):
    CV_name = forms.CharField(max_length=100, label="CV name")
    first_name = forms.CharField(max_length=50, label="First name")
    last_name = forms.CharField(max_length=100, label="Last name")
    current_position = forms.CharField(max_length=70, required=False)
    mobile = forms.CharField(max_length=20)
    email = forms.EmailField(max_length=70)
    date_of_birth = forms.DateField(label="Date of birth")
    address = forms.CharField(max_length=250)
    postal_code = forms.CharField(max_length=10)
    city = forms.CharField(max_length=100)

class ExperienceForm(forms.Form):
    company = forms.CharField(max_length=100, required=False)
    # job_location = forms.CharField(max_length=100, required=False)
    position = forms.CharField(max_length=100, required=False)
    start_date = forms.CharField(required=False)
    end_date = forms.CharField(required=False) 
    description = RichTextFormField(required=False)

class EducationForm(forms.Form):
    institution = forms.CharField(max_length=100, required=False)
    specialisation = forms.CharField(max_length=100, required=False)
    start_date = forms.CharField(required=False)
    end_date = forms.CharField(required=False)
    description = RichTextFormField(required=False)

class SkillForm(forms.Form):
    CHOICES = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5)
    )
    skill = forms.CharField(max_length=30, required=False)
    rating = forms.TypedChoiceField(choices=CHOICES, required=False)

class LicenseForm(forms.Form):
    name = forms.CharField(max_length=50, required=False, label="License or certificate name")
    date_finished = forms.DateField(required=False, label="Date finished", widget=forms.SelectDateWidget)
 
class InterestForm(forms.Form):
    text = RichTextFormField(required=False, label="Interest")

class ClauseForm(forms.Form):
    text = RichTextFormField(required=False, label="Clause")