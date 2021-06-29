from rest_framework import serializers
from .models import (
    Customer,
    DataSheet, 
    Document, 
    Profession
)

class DataSheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataSheet
        fields = [
            'id', 'description', 'historical_data'
        ]


class ProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profession
        fields = ['id', 'description']


class CustomerSerializer(serializers.ModelSerializer):
    data_sheet = DataSheetSerializer()
    professions = ProfessionSerializer(many=True, read_only=True)
    document_set = serializers.StringRelatedField(many=True)

    class Meta:
        model = Customer
        fields = [
            'id', 'name', 'address', 'professions', 'data_sheet',
            'active', 'status_message', 'document_set']


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = [
            'id', 'dtype', 'doc_number', 'customer'
        ]