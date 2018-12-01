from django.db import models

# Create your models here.

class Location(models.Model):
    location_id = models.AutoField(primary_key=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=11)
    longitude = models.DecimalField(max_digits=11)

    class Meta:
        managed = False
        db_table = 'location'
        ordering = ['location']
        verbose_name = 'location'
        verbose_name_plural = 'locations'

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(unique=True, max_length=256)
    review_count = models.IntegerField()
    yelp_since = models.CharField(max_length=256)
    fans = models.IntegerField()
    average_star = models.DecimalField(max_digits=3)
    
    class Meta:
        managed = False
        db_table = 'user'
        ordering = ['user']
        verbose_name = 'user'
        verbose_name_plural = 'users'
    
class Business(models.Model):
    business_id = models.AutoField(primary_key=True)
    business_name = models.CharField(unique=True, max_length=256)
    location = models.ForeignKey(Location, models.DO_NOTHING)
    stars = models.DecimalField(max_digits=3)
    review_count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'business'
        ordering = ['business']
        verbose_name = 'business'
        verbose_name_plural = 'businesses'
    
class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, models.DO_NOTHING)
    business_id = models.ForeignKey(Business, models.DO_NOTHING)
    stars = models.IntegerField()
    text = models.CharField(max_length=10000) # not sure the length
    useful = models.IntegerField()
    funny = models.IntegerField()
    cool = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'review'
        ordering = ['review']
        verbose_name = 'review'
        verbose_name_plural = 'reviews'


    