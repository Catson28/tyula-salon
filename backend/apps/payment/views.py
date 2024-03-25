from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PaymentSerializer, PaymentReportSerializer
from .models import Payment, PaymentReport

@api_view(['GET'])
def payment_list(request):
    payments = Payment.objects.all()
    serializer = PaymentSerializer(payments, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def payment_report_list(request):
    payment_reports = PaymentReport.objects.all()
    serializer = PaymentReportSerializer(payment_reports, many=True)
    return Response(serializer.data)



@api_view(['POST'])
def create_payment(request):
    serializer = PaymentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_payment_report(request):
    serializer = PaymentReportSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Payment, PaymentReport
from .serializers import PaymentSerializer, PaymentReportSerializer
from django.shortcuts import get_object_or_404

class PaymentDetailView(APIView):
    def get(self, request, pk):
        payment = get_object_or_404(Payment, pk=pk)
        serializer = PaymentSerializer(payment)
        return Response(serializer.data)

class PaymentReportDetailView(APIView):
    def get(self, request, pk):
        payment_report = get_object_or_404(PaymentReport, pk=pk)
        serializer = PaymentReportSerializer(payment_report)
        return Response(serializer.data)
