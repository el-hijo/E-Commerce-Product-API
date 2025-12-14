from rest_framework.routers import DefaultRouter
from .views import ShippingAddressViewSet

router = DefaultRouter()
router.register("addresses", ShippingAddressViewSet, basename="shipping-address")

urlpatterns = router.urls
