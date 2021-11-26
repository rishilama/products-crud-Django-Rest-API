from rest_framework import fields, serializers
from . import models as ProductModels


class ProductViewSets(serializers.ModelSerializer):
    class Meta:
        model = ProductModels.Product
        fields ='__all__'