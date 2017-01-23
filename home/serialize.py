__author__ = 'kadgar'
from rest_framework import serializers
from home.models import *


class AuthorSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return Author.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance

    def delete(self):
        pass

    class Meta:
        model = Author
        fields = '__all__'


class BookSerializerManager(serializers.ModelSerializer):
    pass

    class Meta:
        model = Book
        fields = '__all__'

        # fields = ('title', 'author')


class BookSerializer(BookSerializerManager):
    def create(self, validated_data):
        return Book.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.page_size = validated_data.get('page_size', instance.page_size)
        instance.author = validated_data.get('author', instance.author)
        instance.save()
        return instance

    def delete(self):
        pass


class BookAdvancedSerializer(BookSerializerManager, serializers.ModelSerializer):
    author = AuthorSerializer()
