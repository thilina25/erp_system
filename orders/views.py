from django.shortcuts import render
from django.db import transaction
from inventory.models import Product
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from .models import Order, OrderItem, Invoice
from .serializers import OrderSerializer, OrderItemSerializer, InvoiceSerializer
from django.db.models import Sum, Count
from django.utils.timezone import now
from datetime import timedelta
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import OrderItem

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
    
    @transaction.atomic
    def create(self, request, *args, **kwargs):
        date = request.data
        items = data.get("items")
        
        order = Order.objects.create(
            customer_name=data.get("customer_name"),
            status="PENDING",
            total_amount=0
        )
        
        total = 0
        
        for item in items:
            product = Product.objects.get(id=item["product"])
            qty = item ["quantity"]
            
            #Stock Check
            if product.quantity < qty:
                return Response(
                    {"error": f"Not enough stock for {product.name}"},
                    status=status.HTTP_400_BAD_REQUEST
                )
                
            #Deduct Stock
            product.quantity -= qty
            product.save()
            
            price = product.price * qty
            total += price
            
            OrderItem.objecs.create(
                order=order,
                product=product,
                quantity=qty,
                price=product.price
            )
            
            order.total_amount = total
            order.save()
            
            serializer = self.get_serializer(order)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    #Total Sales & Order Count
    @action(detail=False, methods=['get'])
    def dashboard_summery(self, request):
        total_orders = Order.objects.count()
        total_revenue = Order.objects.aaggregate(total=sum('total_amount'))['total'] or 0
        
        return Response({
            "total_orders": total_orders,
            "total_revenue": total_revenue
        })
        
    #Orders Per Day (Last 7 Days)
    @action(detail=False, methods=['get'])
    def orders_last_7_days(self, request):
        last_7_days = now() - timedelta(days=7)
        
        data = (
            Order.objects
            .filter(date__gte=last_7_days)
            .extra(select={'day': 'date(date)'})
            .values('day')
            .annotate(count=Count('id'))
            .order_by('day')
        )
        
        return Response(data)
    
    #Best-Selling Products
    @action(detail=False, methods=['get'])
    def best_selling_products(self, request):
        data = (
            OrderItem.objects
            .values('product__name')
            .annotate(total_sold=Sum('quantity'))
            .order_by('-total_sold')[:5]
        )
        
        return Response(data)
    
    #Monthly Revenue
    @action(detail=False, methods=['get'])
    def monthly_revenue(self, request):
        data = (
            Order.objects
            .extra(select={'month': "strftime('%%m', date)"})
            .value('month')
            .annotate(revenue=Sum('total_amount'))
            .order_by('month')
        )
        
    #Low Stock Summery
    @action(detail=False, methods=['get'])
    def stock_summery(self, request):
        total_products = Product.objects.count()
        low_stock = Product.objects.filter(quantity__lte=models.F('reorder_level')).count()
        
        return Response({
            "total_products": total_products,
            "low_stock_products": low_stock
        })
        
        
class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = [IsAuthenticated]
    
class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    permission_classes = [IsAuthenticated]
    
@action(detail=True, methods=['post'])
def update_status(self, request, pk=None):
    order = self.get_object()
    new_status = request.data.get("status")

    valid_statuses = ['PENDING', 'APPROVED', 'SHIPPED', 'COMPLETED', 'CANCELLED']

    if new_status not in valid_statuses:
        return Response({"error": "Invalid status"}, status=400)

    order.status = new_status
    order.save()

    return Response({"message": "Status updated"})
