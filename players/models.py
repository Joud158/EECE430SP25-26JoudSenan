from django.db import models


class VoleyPlayer(models.Model):
    name = models.CharField(max_length=100)
    date_joined = models.DateField()
    position = models.CharField(max_length=50)
    salary_payment = models.DecimalField(max_digits=10, decimal_places=2)
    contact_person = models.CharField(max_length=100)

    def __str__(self):
        return self.name
