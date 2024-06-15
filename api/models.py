from django.db import models


class Query(models.Model):
    query = models.CharField(max_length=250)
    answer = models.TextField()

    def __str__(self) -> str:
        return f"{self.query}"


class HealthPlan(models.Model):
    weight = models.CharField(max_length=250, null=True, blank=True)
    age = models.CharField(max_length=250, null=True, blank=True)
    medical_history = models.TextField(null=True,blank=True)
    plan = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.id}"