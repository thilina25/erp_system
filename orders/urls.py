from rest_framework.routers import DefaultRouter
from .views import OrderViewSet, OrderItemViewSet, InvoiceViewSet

router = DefaultRouter()
router.register('orders', OrderViewSet)
router.register('order-item', OrderItemViewSet)
router.register('invoices', InvoiceViewSet)

urlpatterns = router.urls
