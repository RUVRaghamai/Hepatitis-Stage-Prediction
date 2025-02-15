from django.contrib import admin

# Register your models here.
# In your app's admin.py
from django.contrib import admin
from .models import HepatitisPrediction

@admin.register(HepatitisPrediction)
class HepatitisPredictionAdmin(admin.ModelAdmin):
    list_display = (
        'user', 
        'jaundice', 
        'fatigue', 
        'nausea', 
        'abdominal_pain', 
        'ascites', 
        'variceal_bleeding', 
        'liver_failure', 
        'hepatocellular_carcinoma', 
        'alt', 
        'ast', 
        'bilirubin', 
        'lfts', 
        'hbsag', 
        'anti_hcv', 
        'anti_hav', 
        'anti_hev', 
        'liver_biopsy', 
        'prediction', 
        
    )
