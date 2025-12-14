from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import OrderViewSet, CreateOrderView

router = DefaultRouter()
router.register("", OrderViewSet, basename="orders")

urlpatterns = [
    path("checkout/", CreateOrderView.as_view(), name="checkout"),
]
urlpatterns += router.urls
