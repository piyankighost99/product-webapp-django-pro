from django.db import models

# Create your models here.


class companyInformation(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self):
        return self.name
    

    
class category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    
class product(models.Model):
    product_name = models.CharField(max_length=100)
    product_description = models.TextField()
    category = models.ForeignKey(category, on_delete=models.CASCADE, related_name='products')
    image = models.ImageField(null=True)
    price = models.FloatField(null=True)
    date = models.DateTimeField(auto_now_add=True, null=True)
    

    def __str__(self):
        return self.product_name
    