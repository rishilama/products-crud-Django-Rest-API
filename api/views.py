from rest_framework import viewsets, response, status
from rest_framework.generics import get_object_or_404
from . import serializers, models as ProductModels


class ProductviewSet(viewsets.ViewSet):

    serializers_class = serializers.ProductViewSets
    queryset = ProductModels.Product.objects.all()

    def list(self, request):
        serializer = self.serializers_class(self.queryset, many=True)
        return response.Response(serializer.data)

    def retrieve(self, request, pk=None):
        product = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializers_class(product)
        return response.Response(serializer.data)

    def create(self, request):
        serializer = self.serializers_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(serializer.data)

    def update(self, request, pk=None):
        product = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializers_class(product, request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(serializer.data)

    def partial_update(self, request, pk=None):
        product = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializers_class(product, request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(serializer.data)

    def destroy(self, request, pk=None):
        product = get_object_or_404(self.queryset, pk=pk)
        product.delete()
        return response.Response(status=status.HTTP_200_OK)