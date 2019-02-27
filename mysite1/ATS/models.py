from django.db import models

# Create your models here.
class Nodes(models.Model):
    node_IP = models.CharField(max_length=200,primary_key=True)
    node_name=models.CharField(max_length=200,blank=True,null=True)
    solution=models.CharField(max_length=200,blank=True,null=True)
    dc=models.CharField(max_length=200,blank=True,null=True)
    box_type=models.CharField(max_length=200,blank=True,null=True)
    pool_name=models.CharField(max_length=200,blank=True,null=True)