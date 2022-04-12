from django.db import models
from django.forms import ValidationError

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=24, null=False, blank=False, unique=True)
    description = models.TextField(max_length=500)

class Subcategory(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')

    def clean(self):
        cleaned_data = super(Subcategory, self).clean()  
        if self.category.subcategories.filter(name=self.name).exists():
            raise ValidationError('Subcategory already exists in this category') 

        return cleaned_data

class Post(models.Model):
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, related_name='posts')
    description = models.TextField(max_length=500)
    image = models.URLField(null=True, blank=True)
    
    def clean(self):
        cleaned_data = super(Post, self).clean()  
        if self.subcategory.posts.filter(description=self.description).exists():
            raise ValidationError('Post already exists in this subcategory') 

        return cleaned_data