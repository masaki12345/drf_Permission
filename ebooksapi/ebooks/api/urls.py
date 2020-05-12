from django.urls import path
from ebooks.api.views import EbookListCreateAPIView, EbookDetailAPIView, ReviewCreateAPIView, ReviewDetailAPIView
urlpatterns = [
    path("ebooks/", EbookListCreateAPIView.as_view()),
    path("ebooks/<int:pk>/", EbookDetailAPIView.as_view()),
    path("ebooks/<int:ebook_pk>/reviews/", ReviewCreateAPIView.as_view()),
    path("reviews/<int:pk>/", ReviewDetailAPIView.as_view())

]
