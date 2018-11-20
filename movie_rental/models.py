from django.db import models

# Create your models here.
class Customers(models.Model):
	firstname=models.CharField(max_length=20)
	lastname=models.CharField(max_length=20)
	email=models.EmailField(max_length=254)
	contact=models.CharField(max_length=10)
	address = models.CharField(max_length=150)  
	city = models.CharField(max_length=150)   
	state = models.CharField(max_length=20)  
	zipcode = models.CharField(max_length=33)  
	country = models.CharField(max_length=150) 

	def __str__(self):
		return self.firstname


		
class Movies(models.Model):
	moviename=models.CharField(max_length=100)
	category=models.CharField(max_length=100)
	price=models.FloatField()
	customer=models.ForeignKey(Customers, on_delete=models.SET_NULL,null=True,blank=True)

	def __str__(self):
		return self.moviename
