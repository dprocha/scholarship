from django.contrib import admin

from .models import ScholarshipInfo
from .models import DataFile

admin.site.register(ScholarshipInfo)
admin.site.register(DataFile)
