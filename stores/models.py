from django.db import models

# Create your models here.
class Store(models.Model):
    regions_in_ghana = [
    ("GAA", "Greater Accra"),
    ("ASH", "Ashanti"),
    ("WES", "Western"),
    ("EAS", "Eastern"),
    ("CEN", "Central"),
    ("VOL", "Volta"),
    ("NOR", "Northern"),
    ("UPE", "Upper East"),
    ("UPW", "Upper West"),
    ("BON", "Bono"),
    ("BNE", "Bono East"),
    ("AHA", "Ahafo"),
    ("SAV", "Savannah"),
    ("NER", "North East")
]


    city = models.CharField(max_length=200)
    region = models.CharField(max_length=100,choices=regions_in_ghana)
    phone_number = models.CharField(max_length=100)
    email = models.EmailField()
    
    def __str__(self) -> str:
        return f"{self.region}-{self.city} store"
    
