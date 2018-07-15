from rest_framework import serializers
from .models import stu


class Serializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'description',
        )
        model =
