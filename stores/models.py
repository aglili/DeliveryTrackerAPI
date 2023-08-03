from django.db import models
from accounts.models import CustomUser
from django.utils import timezone

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

    store_id = models.CharField(primary_key=True,unique=True,max_length=200)
    city = models.CharField(max_length=200)
    region = models.CharField(max_length=100,choices=regions_in_ghana)
    ghp_address = models.CharField(max_length=100,default="GHP-3462-246")
    phone_number = models.CharField(max_length=100)
    email = models.EmailField()
    manager = models.ForeignKey(CustomUser,on_delete=models.SET_NULL,null=True)
    created_at = models.DateTimeField(default=timezone.now, editable=False)

    
    def __str__(self) -> str:
        return f"{self.region}-{self.city} store"
    
    def save(self, *args, **kwargs):
        if not self.store_id:
            last_store_id = Store.objects.order_by("-store_id").first()
            number = (int(last_store_id.store_id.split("-")[1]) + 1) if last_store_id else 1
            self.store_id = f"{self.region}-{number:04d}"

        super().save(*args, **kwargs)

