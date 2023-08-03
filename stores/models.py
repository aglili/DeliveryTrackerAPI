from django.db import models
from accounts.models import CustomUser

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

    id = models.CharField(primary_key=True,unique=True)
    city = models.CharField(max_length=200)
    region = models.CharField(max_length=100,choices=regions_in_ghana)
    phone_number = models.CharField(max_length=100)
    email = models.EmailField()
    manager = models.ForeignKey(CustomUser,on_delete=models.SET_NULL,null=True)

    
    def __str__(self) -> str:
        return f"{self.region}-{self.city} store"
    
    def save(self, *args, **kwargs):
        if not self.id:
            last_store_id = Store.objects.order_by('-id').first()
            number = (last_store_id.id + 1) if last_store_id else 1
            self.id = f"{self.region}-{number:04d}" 

        super().save(*args, **kwargs)
