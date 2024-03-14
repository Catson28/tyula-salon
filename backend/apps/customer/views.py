from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Customer
from .serializers import CustomerSerializer


@api_view(["POST"])
def add_customer(request):
    serializer = CustomerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(["PUT"])
def edit_customer(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    serializer = CustomerSerializer(customer, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


@api_view(["DELETE"])
def delete_customer(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    customer.delete()
    return Response(status=204)


@api_view(["GET"])
def show_customer(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    serializer = CustomerSerializer(customer)
    return Response(serializer.data)


@api_view(["GET"])
def list_customers(request):
    customers = Customer.objects.all()
    serializer = CustomerSerializer(customers, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def search_customer(request):
    # Assuming search functionality will be implemented later
    return Response({"message": "Search functionality not implemented yet."})


@api_view(["GET"])
def associate_customer_with_sale(request):
    # Assuming association functionality will be implemented later
    return Response({"message": "Association functionality not implemented yet."})
