from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Credit, Debit, AccountsReceivable, PendingInvoiceDetails
from .serializers import CreditSerializer, DebitSerializer, AccountsReceivableSerializer, PendingInvoiceDetailsSerializer
from django.shortcuts import get_object_or_404

from .models import Credit, Debit, AccountsReceivable, PendingInvoiceDetails
from .serializers import (
    CreditSerializer,
    DebitSerializer,
    AccountsReceivableSerializer,
    PendingInvoiceDetailsSerializer,
)

@api_view(['GET'])
def credit_list(request):
    credits = Credit.objects.all()
    serializer = CreditSerializer(credits, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def debit_list(request):
    debits = Debit.objects.all()
    serializer = DebitSerializer(debits, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def accounts_receivable_list(request):
    accounts_receivable = AccountsReceivable.objects.all()
    serializer = AccountsReceivableSerializer(accounts_receivable, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def pending_invoice_details_list(request):
    pending_invoice_details = PendingInvoiceDetails.objects.all()
    serializer = PendingInvoiceDetailsSerializer(pending_invoice_details, many=True)
    return Response(serializer.data)



@api_view(['POST'])
def create_credit(request):
    serializer = CreditSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_debit(request):
    serializer = DebitSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_accounts_receivable(request):
    serializer = AccountsReceivableSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_pending_invoice_details(request):
    serializer = PendingInvoiceDetailsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CreditDetailView(APIView):
    def get(self, request, pk):
        credit = get_object_or_404(Credit, pk=pk)
        serializer = CreditSerializer(credit)
        return Response(serializer.data)

class DebitDetailView(APIView):
    def get(self, request, pk):
        debit = get_object_or_404(Debit, pk=pk)
        serializer = DebitSerializer(debit)
        return Response(serializer.data)

class AccountsReceivableDetailView(APIView):
    def get(self, request, pk):
        accounts_receivable = get_object_or_404(AccountsReceivable, pk=pk)
        serializer = AccountsReceivableSerializer(accounts_receivable)
        return Response(serializer.data)

class PendingInvoiceDetailsDetailView(APIView):
    def get(self, request, pk):
        pending_invoice_details = get_object_or_404(PendingInvoiceDetails, pk=pk)
        serializer = PendingInvoiceDetailsSerializer(pending_invoice_details)
        return Response(serializer.data)



