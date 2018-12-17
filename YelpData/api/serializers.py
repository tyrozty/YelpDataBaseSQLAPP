from YelpData.models import Location, Business, User, Review, Tip, Photo
from rest_framework import response, serializers, status


class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields = ('location_id', 'location_identifier', 'city', 'state', 'postal_code', 'latitude', 'longitude')


class BusinessSerializer(serializers.ModelSerializer):
    location = LocationSerializer(many=False, read_only=True)

    class Meta:
        model = Business
        fields = ('business_id', 'business_identifier', 'business_name', 'location', 'stars', 'review_count')


class UserSerializer(serializers.ModelSerializer):
    user_identifier = serializers.CharField(
		allow_blank=False,
		max_length=255
	)
    user_name = serializers.CharField(
        allow_blank=False,
        max_length=255
    )
    review_count = serializers.IntegerField(
        allow_null=False
    )
    yelping_since = serializers.CharField(
        allow_blank=False,
        max_length=255 
    )
    fans = serializers.IntegerField(
        allow_null=False
    )
    average_stars = serializers.CharField(
        allow_blank=False,
        max_length=3
    )

    class Meta:
        model = User
        fields = ('user_id', 'user_identifier', 'user_name', 'review_count', 'yelping_since', 'fans', 'average_stars')

    def create(self, validated_data):
        buinesses = validated_data.pop('review')
        user = User.objects.create(**validated_data)

        if businesses is not None:
            for business in businesses:
                Review.objects.create(
                    user_id = user.user_id,
                    business = business.business_id
                ) 
        return user

    def update(self, instance, validated_data):
        user_id = instance.user_id
        new_businesses = validated_data.pop('review')
        instance.user_identifier = validated_data.get(
            'user_identifier',
            instance.user_identifier
            )
        instance.user_name = validated_data.get(
            'user_name',
            instance.user_name
        )
        instance.review_count = validated_data.get(
            'review_count',
            instance.review_count
        )
        instance.yelping_since = validated_data.get(
            'yelping_since',
            instance.yelping_since
        )
        instance.fans = validated_data.get(
            'fans',
            instance.fans
        )
        instance.average_stars = validated_data.get(
            'average_stars',
            instance.average_stars
        )

        new_ids = []
        old_ids = Review.objects\
        .values_list('business_id', flat=True)\
        .filter(user_id__exact=user_id)

        for business in new_businesses:
            new_id = business.business_id
            new_ids.append(new_id)
            if new_id in old_ids:
                continue
            else:
                Review.objects\
                .create(user_id=user_id, business_id=business_id)
        
        for old_id in old_ids:
            if old_id in new_ids:
                continue
            else:
                Review.objects\
                .filter(user_id=user_id, business_id=business_id)\
                .delete()
        return instance


class ReviewSerializer(serializers.ModelSerializer):
    user_id = UserSerializer(many=False, read_only=True)#UserSerializer.ReadOnlyField(source='user.user_id')
    business_id = BusinessSerializer(many=False, read_only=True)#BusinessSerializer.ReadOnlyField(source='business.business_id')

    class Meta:
        model = Review
        fields = ('review_id', 'review_identifier', 'user', 'business', 'stars', 'text', 'useful', 'funny', 'cool')


class TipSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)
    business = BusinessSerializer(many=False, read_only=True)
    class Meta:
        model = Tip
        fields = ('tip_id', 'text', 'date', 'likes', 'business', 'user')


class PhotoSerializer(serializers.ModelSerializer):
    business = BusinessSerializer(many=False, read_only=True)
    class Meta:
        model = Photo
        fields = ('photo_id', 'photo_identifier', 'business', 'caption', 'label')

		