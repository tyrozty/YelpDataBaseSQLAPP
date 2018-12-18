from django.db import models
from django.urls import reverse


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
    location = models.ForeignKey(Location, on_delete=models.PROTECT)
    stars = models.CharField(max_length=3)
    review_count = models.IntegerField()
    description = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'business'
        verbose_name = 'business'
        verbose_name_plural = 'businesses'


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_identifier = models.CharField(unique=True, max_length=255)
    user_name = models.CharField(max_length=255)
    review_count = models.IntegerField()
    yelping_since = models.CharField(max_length=256)
    fans = models.IntegerField()
    average_stars = models.CharField(max_length=3)
    
    business = models.ManyToManyField(
        Business,
        through='Review'
    ) 

    class Meta:
        managed = False
        db_table = 'user'
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def __str__(self):
        return self.user_name

    def get_absolute_url(self):
        return reverse('user_detail', kwargs={'pk': self.pk})

    @property
    def business_names(self):
        businesses = self.business.select_related('location').order_by('business_name')
        names = []
        for business in businesses:
            name = business.business_name
            if name is None:
                continue
            if name not in names:
                names.append(name)
        return ', '.join(names)

   #TODO: adding more properties?


class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    review_identifier = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    stars = models.IntegerField()
    text = models.CharField(max_length=10000) # not sure the length
    useful = models.IntegerField()
    funny = models.IntegerField()
    cool = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'review'
        verbose_name = 'review'
        verbose_name_plural = 'reviews'


class Tip(models.Model):
    tip_id = models.AutoField(primary_key=True)
    text = models.CharField(max_length=1024)
    date = models.CharField(max_length=100)
    likes = models.IntegerField()
    business = models.ForeignKey(Business, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    class Meta:
        managed = False
        db_table = 'tip'
        verbose_name = 'tip'
        verbose_name_plural = 'tips'

class Photo(models.Model):
    photo_id = models.AutoField(primary_key=True)
    photo_identifier = models.CharField(max_length=1024)
    business = models.ForeignKey(Business, on_delete=models.PROTECT)
    caption = models.CharField(max_length=1024)
    label = models.CharField(max_length=1024)

    class Meta:
        managed = False
        db_table = 'photo'
        verbose_name = 'photo'
        verbose_name_plural = 'photos'
    
    