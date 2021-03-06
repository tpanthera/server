from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """
    User object serializer class
    """
    class Meta(object):
        model = User
        fields = ('username', 'first_name', 'last_name', 'id')
