from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from base.models import Product, Order, OrderItem, ShippingAddress
from base.serializers import ProductSerializer, OrderSerializer

from rest_framework import status


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addOrderItems(request):
    user = request.user
    data = request.data
    orderItems = data['orderItems']

    print(data)
    if orderItems and len(orderItems) == 0:
        return Response({'detail': 'No Order Items'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        order = Order.objects.create(
            user=user,
            payment_method=data['payment_method'],
            tax_price=10, #data['tax_price'],
            total_price=10 #data['total_price']
        )

        shippingAddress = ShippingAddress.objects.create(
            order=order,
            address=data['shipping_address']['address'],
            zip_code=data['shipping_address']['postalCode'],
            city=data['shipping_address']['address']
            #country=data['shipping_address']['country']
        )

        for i in orderItems:
            product = Product.objects.get(_id=i['product'])

            item = OrderItem.objects.create(
                product=product,
                order=order,
                name=product.title,
                price=10, #product.price,
            )
        serializer = OrderSerializer(order, many=False)
        return Response(serializer.data)
