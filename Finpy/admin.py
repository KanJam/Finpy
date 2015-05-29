from django.contrib import admin
from Finpy.models import Category, Entry, UserProfile, Finance, InvestmentSimulation

# Register your models here
admin.site.register(Category)
admin.site.register(Entry)
admin.site.register(UserProfile)
admin.site.register(Finance)
admin.site.register(InvestmentSimulation)