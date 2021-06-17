from rest_framework import serializers
from .models import Hero


class HeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hero
        fields = ['id', 'name', 'alias']

    # for serializers.Serializer
    # def create(self, validated_data):
    #     """
    #     Create and return a new `Snippet` instance, given the validated data.
    #     """
    #     return Hero.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     """
    #     Update and return an existing `Snippet` instance, given the validated data.
    #     """
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.alias = validated_data.get('alias', instance.alias)
    #     instance.save()
    #     return instance
