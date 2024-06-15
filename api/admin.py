from django.contrib import admin

from .models import Query, HealthPlan

admin.site.register([Query, HealthPlan])
