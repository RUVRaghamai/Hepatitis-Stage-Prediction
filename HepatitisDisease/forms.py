from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django.contrib.auth.models import User



class LoginForm (AuthenticationForm):
        username =UsernameField(widget=forms.TextInput(attrs={'autofocus': 'True' ,'class': 'form-control'}))
        password=forms.CharField(widget=forms.PasswordInput(attrs= {'autocomplete': 'current-password', 'class': 'form-control'}))

class CustomerRegistrationForm(UserCreationForm):
       username = forms.CharField(widget=forms.TextInput(attrs={'autofocus ': 'True', 'class': 'form-control'}))
       email= forms.EmailField(widget=forms.EmailInput(attrs= {'class': 'form-control'}))
       password1=forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
       password2=forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
       
from django import forms

class HepatitisForm(forms.Form):
    Jaundice = forms.ChoiceField(choices=[(0, 'No'), (1, 'Yes')])
    Fatigue = forms.ChoiceField(choices=[(0, 'No'), (1, 'Yes')])
    Nausea = forms.ChoiceField(choices=[(0, 'No'), (1, 'Yes')])
    Abdominal_Pain = forms.ChoiceField(choices=[(0, 'No'), (1, 'Yes')])
    Ascites = forms.ChoiceField(choices=[(0, 'No'), (1, 'Yes')])
    Variceal_Bleeding = forms.ChoiceField(choices=[(0, 'No'), (1, 'Yes')])
    Liver_Failure = forms.ChoiceField(choices=[(0, 'No'), (1, 'Yes')])
    Hepatocellular_Carcinoma = forms.ChoiceField(choices=[(0, 'No'), (1, 'Yes')])
    ALT = forms.FloatField()
    AST = forms.FloatField()
    Bilirubin = forms.FloatField()
    LFTs = forms.ChoiceField(choices=[(1, 'Normal'), (2, 'Abnormal'), (3, 'Severely Abnormal')])
    HBsAg = forms.ChoiceField(choices=[(0, 'Negative'), (1, 'Positive')])
    anti_HCV = forms.ChoiceField(choices=[(0, 'Negative'), (1, 'Positive')])
    anti_HAV = forms.ChoiceField(choices=[(0, 'Negative'), (1, 'Positive')])
    anti_HEV = forms.ChoiceField(choices=[(0, 'Negative'), (1, 'Positive')])
    Liver_Biopsy = forms.ChoiceField(choices=[(1, 'Normal'), (2, 'Inflammation'), (3, 'Fibrosis'),(4,'Cirrhosis')])
