from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from base.models import Product
from base.serializers import ProductSerializer


@api_view(['GET'])
def get_products(request):
    query = request.query_params.get('keyword')
    if query == None:
        query = ''
    products = Product.objects.filter(title__icontains=query)

    page = request.query_params.get('page')
    paginator = Paginator(products, 3)

    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    if page == None:
        page = 1

    page = int(page)

    serializer = ProductSerializer(products, many=True)
    return Response({'products': serializer.data, 'page': page, 'pages': paginator.num_pages})


@api_view(['GET'])
def get_product(request, pk):
    product = Product.objects.get(_id=pk)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAdminUser])
def create_product(request):
    user = request.user
    product = Product.objects.create(
        user=user,
        title='Sample Name',
        price=10,
        description="Hello, World",
        is_soundkit=False,
    )

    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)


@api_view(['PUT'])
@permission_classes([IsAdminUser])
def update_product(request, pk):
    data = request.data
    product = Product.objects.get(_id=pk)

    print(data)
    product.title = data['title']
    product.price = data['price']
    product.description = data['description']

    product.save()

    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def delete_product(request, pk):
    product = Product.objects.get(_id=pk)
    product.delete()
    return Response('Product deleted')


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


@api_view(['POST'])
@permission_classes([IsAdminUser])
def upload_image(request):
    data = request.data
    product_id = data['product_id']
    product = Product.objects.get(_id=product_id)
    product.image = request.FILES.get('image')
    product.save()
    return Response('Image was uploaded')


@api_view(['POST'])
@permission_classes([IsAdminUser])
def upload_file(request):
    data = request.data
    product_id = data['product_id']
    product = Product.objects.get(_id=product_id)
    product.file = request.FILES.get('file')
    product.save()
    return Response('Image was uploaded')
