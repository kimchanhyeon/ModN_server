from rest_framework import serializers

from ModN.catalog.models import Market, Seller

class MarketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Market

class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
