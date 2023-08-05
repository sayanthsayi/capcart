from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='category_img')
    description = models.CharField(max_length=500)
    slug = models.SlugField()

    def __str__(self):
        return self.name
    

class SubCategory(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='subcat_image')
    category =models.ForeignKey(Category,on_delete=models.CASCADE)
    slug = models.SlugField()

    def __str__(self):
        return '{}-{}'.format(self.name,self.category.name)   
    
class ProductSeries(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='Productseries_img')
    description = models.CharField(max_length=500,null=True,blank=True)
    slug = models.SlugField()
    subcategory = models.ForeignKey(SubCategory,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Products(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='product_img',null=True,blank=True)
    image2 = models.ImageField(upload_to='product_img2',null=True,blank=True)
    image3 = models.ImageField(upload_to='product_img3',null=True,blank=True)
    image4= models.ImageField(upload_to='product_img4',null=True,blank=True)
    description = models.CharField(max_length=500)
    disc_price = models.IntegerField()
    org_price = models.IntegerField()
    qty = models.IntegerField()
    slug = models.SlugField()
    subcategory = models.ForeignKey(SubCategory,on_delete=models.CASCADE)
    category =models.ForeignKey(Category,on_delete=models.CASCADE)
    productseries = models.ForeignKey(ProductSeries,on_delete=models.CASCADE)


    def __str__(self):
        return self.name 
    


