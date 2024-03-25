from rest_framework import serializers
from .models import Payment, PaymentReport

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['id', 'date', 'paid']

class PaymentReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentReport
        fields = ['id', 'type']
