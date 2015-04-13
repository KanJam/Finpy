from django.contrib import admin
from Finpy.models import Entry, UserProfile, Periodicity, CategoryRecord

admin.site.register(Entry)
admin.site.register(Periodicity)
admin.site.register(CategoryRecord)
admin.site.register(UserProfile)
# Register your models here.
