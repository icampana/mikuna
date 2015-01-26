from django.contrib import admin

from accounting.models import Customer, Tax

class CustomerAdmin(admin.ModelAdmin):
    pass

class TaxAdmin(admin.ModelAdmin):
    pass

admin.site.register(Tax, TaxAdmin)
admin.site.register(Customer, CustomerAdmin)