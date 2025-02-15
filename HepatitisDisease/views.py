from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import CustomerRegistrationForm, LoginForm
from django.db import IntegrityError
from django.contrib.auth.views import LoginView

def home(request):
    return render(request, "home.html")

class CustomerRegistrationView(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        return render(request, "customerregistration.html", {'form': form})

    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            try:
                # Create the new user
                new_user = User.objects.create_user(
                    username=form.cleaned_data['username'],
                    password=form.cleaned_data['password2'],
                    email=form.cleaned_data['email']
                )
                return redirect('login')  # Redirect to the login page after successful registration
            except IntegrityError:
                messages.warning(request, "Username or Email already taken. Please try a different one.")
        else:
            messages.warning(request, "Invalid input data")

        return render(request, "customerregistration.html", {'form': form})

class CustomLoginView(LoginView):
    template_name = "login.html"
    authentication_form = LoginForm

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:
            try:
                user = User.objects.get(username=username)
                user = authenticate(username=username, password=password)
                
                if user is not None:
                    login(request, user)
                    return redirect('home')  # Redirect to home page if credentials are correct
                else:
                    messages.error(request, 'Incorrect password. Please try again.')
            except User.DoesNotExist:
                messages.error(request, 'User does not exist. Please check your username or register.')
        else:
            messages.warning(request, 'Please enter both username and password.')

        return render(request, self.template_name, {'form': self.authentication_form})


def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to login page after logout

from .forms import HepatitisForm

def predict_stage(request):
    if request.method == 'POST':
        form = HepatitisForm(request.POST)
        if form.is_valid():
            # Perform prediction logic here
            # Example: jaundice = form.cleaned_data['jaundice']
            # Add logic to process the form and predict the stage
            pass
    else:
        form = HepatitisForm()

    return render(request, 'predict_stage.html', {'form': form})


from django.shortcuts import render
import numpy as np
import pandas as pd
from .forms import HepatitisForm

# Assuming the model and scaler have already been loaded
import joblib
model = joblib.load('C:/Users/raghamairvu/OneDrive/Desktop/FINALYEARPROJECT/project/Finalyear/Hepatitis/scripts/trained_model.pkl')
scaler = joblib.load('C:/Users/raghamairvu/OneDrive/Desktop/FINALYEARPROJECT/project/Finalyear/Hepatitis/scripts/scaler.pkl')


from .models import HepatitisPrediction

def predict_stage(request):
    if request.method == 'POST':
        form = HepatitisForm(request.POST)
        if form.is_valid():
            # Collect form data
            data = {
                'Jaundice': form.cleaned_data['Jaundice'],
                'Fatigue': form.cleaned_data['Fatigue'],
                'Nausea': form.cleaned_data['Nausea'],
                'Abdominal_Pain': form.cleaned_data['Abdominal_Pain'],
                'Ascites': form.cleaned_data['Ascites'],
                'Variceal_Bleeding': form.cleaned_data['Variceal_Bleeding'],
                'Liver_Failure': form.cleaned_data['Liver_Failure'],
                'Hepatocellular_Carcinoma': form.cleaned_data['Hepatocellular_Carcinoma'],
                'ALT': form.cleaned_data['ALT'],
                'AST': form.cleaned_data['AST'],
                'Bilirubin': form.cleaned_data['Bilirubin'],
                'LFTs': form.cleaned_data['LFTs'],
                'HBsAg': form.cleaned_data['HBsAg'],
                'anti-HCV': form.cleaned_data['anti_HCV'],
                'anti-HAV': form.cleaned_data['anti_HAV'],
                'anti-HEV': form.cleaned_data['anti_HEV'],
                'Liver_Biopsy': form.cleaned_data['Liver_Biopsy']
            }

            # Convert data to the format expected by the model
            input_data = np.array([list(data.values())])
            input_data_scaled = scaler.transform(input_data)

            # Make the prediction
            prediction = model.predict(input_data_scaled)
            stage = prediction[0]

            # Mapping stage numbers to stage names
            stage_mapping = {
                0: 'No Hepatitis',
                1: 'Incubation',
                2: 'Acute Hepatitis',
                3: 'Chronic Hepatitis',
                4: 'Advanced Stage of Hepatitis',
                5: 'End Stage of Hepatitis'
            }

            # Get the stage name from the mapping
            predicted_stage_name = stage_mapping.get(stage, 'Unknown')

            # Save the prediction to the database
            HepatitisPrediction.objects.create(
                user=request.user,
                jaundice=data['Jaundice'],
                fatigue=data['Fatigue'],
                nausea=data['Nausea'],
                abdominal_pain=data['Abdominal_Pain'],
                ascites=data['Ascites'],
                variceal_bleeding=data['Variceal_Bleeding'],
                liver_failure=data['Liver_Failure'],
                hepatocellular_carcinoma=data['Hepatocellular_Carcinoma'],
                alt=data['ALT'],
                ast=data['AST'],
                bilirubin=data['Bilirubin'],
                lfts=data['LFTs'],
                hbsag=data['HBsAg'],
                anti_hcv=data['anti-HCV'],
                anti_hav=data['anti-HAV'],
                anti_hev=data['anti-HEV'],
                liver_biopsy=data['Liver_Biopsy'],
                prediction=stage
            )

            # Pass the predicted stage name to the template
            return render(request, 'result.html', {'stage': predicted_stage_name})
    else:
        form = HepatitisForm()

    return render(request, 'predict_stage.html', {'form': form})

 
def result(request):
    # Extract the predicted stage from the request context or session if necessary
    predicted_stage = request.session.get('predicted_stage', 'Unknown')
    
    return render(request, 'result.html', {'predicted_stage': predcited_stage})
