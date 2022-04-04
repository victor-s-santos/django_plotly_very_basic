from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Pessoa(models.Model):
    nome = models.CharField(max_length=250)
    altura = models.FloatField(validators=[MinValueValidator(1.0), MaxValueValidator(3.0)])
    peso = models.FloatField(validators=[MinValueValidator(20.0), MaxValueValidator(600.0)],)
    
    def __str__(self):
        return self.nome

# Create your models here.
