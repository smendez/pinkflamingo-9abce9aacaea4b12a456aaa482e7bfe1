from __future__ import division

from django.contrib.auth.models import User

from rest_framework import serializers

from pinkflamingo.models import Book, Publisher, Author, Rating


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('pk', 'username', 'email', 'groups',)


class BookSerializer(serializers.ModelSerializer):
    # average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = ('pk', 'title', 'description', 'isbn', 'authors', 'publisher', 'average_rating', )
        read_only_fields = ('average_rating', )

    # def get_average_rating(self, obj):
    #     rating_values = Rating.objects.values_list('rating', flat=True).filter(book__pk=obj.pk)
    #
    #     try:
    #         return round(sum(rating_values)/len(rating_values), 1)
    #     except ZeroDivisionError:
    #         return 0


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = ('pk', 'name',)


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ('pk', 'name',)


class RatingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rating
        fields = ('user', 'book', 'rating')


class AuthorBooksSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Author
        fields = ('url', 'name', 'books')
