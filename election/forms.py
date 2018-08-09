from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Election, Alternative, Vote, Question


class Custom_UserCreationForm(UserCreationForm):
    pass

class Choose_Election_Method_And_Name(forms.ModelForm):
    class Meta:
        model = Election
        fields = ('Name', 'Description')

class Edit_Election(forms.ModelForm):
    class Meta:
        model = Election
        fields = ('Name', 'Description')

class Add_Question(forms.ModelForm):
    CHOICES = (('majority','Traditional Majority (NOT RECOMMENDED!)'),
               ('range','Range Voting'),
               ('approval','Approval Voting '),)
    method = forms.MultipleChoiceField(choices=CHOICES, widget=forms.CheckboxSelectMultiple())
    class Meta:
        model = Question
        fields = ('Wording',)

class Create_Alternative(forms.ModelForm):
    class Meta:
        model = Alternative
        fields = ('Wording',)

class Add_Alternative(forms.Form):
    CHOICES =( ('alt', 'Add Alternative'),)
    add = forms.MultipleChoiceField(choices=CHOICES, widget=forms.CheckboxSelectMultiple())
