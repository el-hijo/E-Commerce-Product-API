from django.urls import path
from .views import InitializePaymentView, VerifyPaymentView

urlpatterns = [
    path("init/", InitializePaymentView.as_view(), name="payment-init"),
    path("verify/", VerifyPaymentView.as_view(), name="payment-verify"),
]
