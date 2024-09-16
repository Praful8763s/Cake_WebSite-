from django.contrib import admin
from Cake_Website.models import Contact

# Optionally, create a custom admin class to enhance the admin interface
admin.site.register(Contact)  # Use the custom admin class
