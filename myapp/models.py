from django.db import models

# Create your models here.

class BlogPost(models.Model):
    p_id = models.AutoField(primary_key=True)
    print(p_id)
    p_title = models.CharField(max_length=50)
    p_content0 = models.CharField(max_length=200, default="")
    p_heading = models.CharField(max_length=100, default="")
    p_content1 = models.CharField(max_length=500, default="")
    p_subhead0 = models.CharField(max_length=100, default="")
    p_content2 = models.CharField(max_length=500, default="")
    p_subhead1 = models.CharField(max_length=100, default="")
    p_content3 = models.CharField(max_length=500, default="")
    p_thumb = models.ImageField(upload_to='static/images',default="")

    def __str__(self):
        return self.p_title

    
    
    