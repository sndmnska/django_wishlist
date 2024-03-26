from django.contrib import admin
from .models import Place

# create an administrator to access the Admin console.  ($> python manage.py createsuperuser)
# Note that email can be left blank.  
admin.site.register(Place) 