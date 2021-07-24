from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from base.models import Product
from base.serializers import ProductSerializer


@api_view(['GET'])
def get_products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_product(request, pk):
    product = Product.objects.get(_id=pk)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def get_beats(request):
    beats = Product.objects.filter(is_soundkit=False)
    serializer = ProductSerializer(beats, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_soundkits(request):
    soundkits = Product.objects.filter(is_soundkit=True)
    serializer = ProductSerializer(soundkits, many=True)
    return Response(serializer.data)

