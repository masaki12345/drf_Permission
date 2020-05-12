from ..models import Ebook, Review
from ebooks.api.serializers import EbookSerializers, ReviewSerializers

from rest_framework import generics
from rest_framework import mixins
from rest_framework.generics import get_object_or_404
from rest_framework import permissions
from ebooks.api.permissions import IsAdminUserOrReadOnly


class EbookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Ebook.objects.all()
    serializer_class = EbookSerializers
    permission_classes = [IsAdminUserOrReadOnly]


class EbookDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ebook.objects.all()
    serializer_class = EbookSerializers
    permission_classes = [IsAdminUserOrReadOnly]


class ReviewCreateAPIView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializers

    def perform_create(self, serializer):
        ebook_pk = self.kwargs.get("ebook_pk")
        print("#####################################################################################")
        print(self.kwargs)
        print("#####################################################################################")
        ebook = get_object_or_404(Ebook, pk=ebook_pk)
        serializer.save(ebook=ebook)


class ReviewDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializers
    # class EbookListCreateAPIView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    #     queryset = Ebook.objects.all()
    #     serializer_class = EbookSerializers

    #     def get(self, request, *args, **kwargs):
    #         return self.list(request, *args, **kwargs)

    #     def post(self, request, *args, **kwargs):
    #         return self.create(request, *args, **kwargs)
