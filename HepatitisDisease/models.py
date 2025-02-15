from django.db import models
from django.contrib.auth.models import User


# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class HepatitisPrediction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    jaundice = models.BooleanField()
    fatigue = models.BooleanField()
    nausea = models.BooleanField()
    abdominal_pain = models.BooleanField()
    ascites = models.BooleanField()
    variceal_bleeding = models.BooleanField()
    liver_failure = models.BooleanField()
    hepatocellular_carcinoma = models.BooleanField()
    alt = models.FloatField()
    ast = models.FloatField()
    bilirubin = models.FloatField()
    lfts = models.CharField(max_length=20)
    hbsag = models.BooleanField()
    anti_hcv = models.BooleanField()
    anti_hav = models.BooleanField()
    anti_hev = models.BooleanField()
    liver_biopsy = models.CharField(max_length=20)
    prediction = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.prediction}"
