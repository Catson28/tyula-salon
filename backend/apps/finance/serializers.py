from rest_framework import serializers
from .models import Credit, Debit, AccountsReceivable, PendingInvoiceDetails

class CreditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Credit
        fields = ['id', 'Credit_Reason', 'Credit_Amount', 'Credit_Date', 'seller', 'customer']

class DebitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Debit
        fields = ['id', 'Debit_Reason', 'Debit_Amount', 'Debit_Date', 'seller', 'customer']

class AccountsReceivableSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountsReceivable
        fields = ['id', 'customer', 'Total_Amount_Pending']

class PendingInvoiceDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PendingInvoiceDetails
        fields = ['id', 'Due_Date', 'Invoice_Amount', 'Receivable_Account_ID', 'Invoice_ID']
