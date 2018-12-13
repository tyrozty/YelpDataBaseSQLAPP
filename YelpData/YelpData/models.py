from django.db import models

# Create your models here.

class Location(models.Model):
    location_id = models.AutoField(primary_key=True)
    location_identifier = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=100)
    latitude = models.CharField(max_length=11)
    longitude = models.CharField(max_length=11)

    class Meta:
        managed = False
        db_table = 'location'
        #ordering = ['location']
        verbose_name = 'location'
        verbose_name_plural = 'locations'

    
class Business(models.Model):
    business_id = models.AutoField(primary_key=True)
    business_identifier = models.CharField(max_length=255)
    business_name = models.CharField(unique=True, max_length=255)
    location = models.ForeignKey(Location, models.DO_NOTHING)
    stars = models.CharField(max_length=3)
    review_count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'business'
        #ordering = ['business']
        verbose_name = 'business'
        verbose_name_plural = 'businesses'


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_identifier = models.CharField(max_length=255)
    user_name = models.CharField(unique=True, max_length=255)
    review_count = models.IntegerField()
    yelping_since = models.CharField(max_length=256)
    fans = models.IntegerField()
    average_stars = models.CharField(max_length=3)

    businesses = models.ManyToManyField(
        Business,
        through='Review',
        related_name='users' 
    ) 
    class Meta:
        managed = False
        db_table = 'user'
        #ordering = ['user']
        verbose_name = 'user'
        verbose_name_plural = 'users'


class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    review_identifier = models.CharField(max_length=255)
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
        #ordering = ['review']
        verbose_name = 'review'
        verbose_name_plural = 'reviews'



class Tip(models.Model):
    tip_id = models.AutoField(primary_key=True)
    text = models.CharField(max_length=1024)
    date = models.CharField(max_length=100)
    likes = models.IntegerField()
    business_id = models.ForeignKey(Business, models.DO_NOTHING)
    user_id = models.ForeignKey(User, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'tip'
        verbose_name = 'tip'
        verbose_name_plural = 'tips'

class Photo(models.Model):
    photo_id = models.AutoField(primary_key=True)
    photo_identifier = models.CharField(max_length=255)
    business_id = models.ForeignKey(Business, models.DO_NOTHING)
    caption = models.CharField(max_length=1024)
    label = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'photo'
        verbose_name = 'photo'
        verbose_name_plural = 'photos'
    


    