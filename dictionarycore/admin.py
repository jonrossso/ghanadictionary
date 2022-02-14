import imp
from django.contrib import admin
from .models import translation

# Model Registration
admin.site.register(translation)
