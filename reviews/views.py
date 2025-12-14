from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Review
from .serializers import ReviewSerializer
# Create your views here.


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        product_id = self.request.query_params.get("product")
        queryset = Review.objects.filter(is_approved=True)

        if product_id:
            queryset = queryset.filter(product_id=product_id)

        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
