from django.db import models

# Create your models here.
class Category(models.Model):
    """Contains just the name of the category."""
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Tag(models.Model):
    """Contains just the name of the tag."""
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    """Contains the name of the product, fk to a category, manytomany for multiple tags, and a description."""
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    tags = models.ManyToManyField(Tag, blank=True)
    description = models.TextField() 
    
    def __str__(self):
        return self.name