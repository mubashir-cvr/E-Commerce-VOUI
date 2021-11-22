
from django.db import models
  

class MainCategory(models.Model):
    name =models.CharField(max_length=225)

class GenderCategory(models.Model):
    parentCategory = models.ForeignKey(MainCategory,on_delete=models.CASCADE)
    gender=models.CharField(max_length=20)

class SubCategory(models.Model):
    parentCategory = models.ForeignKey(GenderCategory,on_delete=models.CASCADE)
    name=models.CharField(max_length=225)
    type=models.CharField(max_length=225)
    hasSubcategory = models.BooleanField(default=True)

class SubSubCategory(models.Model):
    parentCategory = models.ForeignKey(SubCategory,on_delete=models.CASCADE)
    gender=models.CharField(max_length=20)

class GeeksModel(models.Model):
    title = models.CharField(max_length = 200)
    description = models.TextField()
  
    def __str__(self):
        return self.title