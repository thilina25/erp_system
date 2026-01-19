from django.shortcuts import render
from django.db import transaction
from inventory.models import Product
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from .models import Order, OrderItem, Invoice
from .serializers import OrderSerializer, OrderItemSerializer, InvoiceSerializer


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
        
class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = [IsAuthenticated]
    
class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    permission_classes = [IsAuthenticated]