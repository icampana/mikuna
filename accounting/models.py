from django.db import models

DOCUMENTS_TYPE =(
    ('p', 'Passport'),
    ('d', 'National Identification Document'),
    ('l', 'Driver\'s License'),
)

class Customer(models.Model):
    name = models.CharField(max_length = 200)
    address = models.TextField(max_length = 200)
    phone = models.CharField(max_length = 20)
    document_id = models.CharField(max_length = 40)
    document_type = models.CharField(max_length = 3, choices = DOCUMENTS_TYPE)
    email = models.EmailField(null = True, blank = True)
    
    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Customers'

class Tax(models.Model):
    name = models.CharField(max_length = 100)
    percentage = models.DecimalField(max_digits = 10, decimal_places = 2, blank = True, null = True)
    
    def __unicode__(self):
        return "%s (%d %%)" % (self.name, self.percentage)

    class Meta:
        verbose_name_plural = 'Taxes'
