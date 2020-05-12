from rest_framework import serializers
from ..models import Ebook, Review


class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        exclude = ("ebook",)
        # fields = "__all__"


class EbookSerializers(serializers.ModelSerializer):

    reviews = ReviewSerializers(many=True, read_only=True)

    class Meta:
        model = Ebook
        fields = "__all__"
