from django.contrib import admin
from .models import companyInformation, category, product

admin.site.register(companyInformation)
admin.site.register(category)
admin.site.register(product)     