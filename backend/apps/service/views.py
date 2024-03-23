from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Service
from .serializers import ServiceSerializer, ServiceProductSerializer
from apps.product.models import Product
from apps.product.serializers import ProductSerializer


@api_view(["GET"])
def list_services(request):
    services = Service.objects.all()
    serializer = ServiceSerializer(services, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def create_service(request):
    serializer = ServiceSerializer(data=request.data)
    print(request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["PUT"])
def update_service(request, service_id):
    service = get_object_or_404(Service, pk=service_id)
    serializer = ServiceSerializer(service, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def retrieve_service(request, service_id):
    service = get_object_or_404(Service, pk=service_id)
    serializer = ServiceSerializer(service)
    return Response(serializer.data)


@api_view(["DELETE"])
def delete_service(request, service_id):
    service = get_object_or_404(Service, pk=service_id)
    service.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["POST"])
def upload_service_image(request, service_id):
    # Logic for uploading service image
    pass


@api_view(["DELETE"])
def delete_service_image(request, image_id):
    # Logic for deleting service image
    pass


@api_view(["POST"])
def select_service_cover_image(request, service_id):
    # Logic for selecting service cover image
    pass


@api_view(["POST"])
def select_or_upload_raw_material(request, service_id):
    # Logic for selecting or uploading raw material for a service
    pass


@api_view(["POST"])
def select_or_upload_categories(request, service_id):
    # Logic for selecting or uploading categories or subcategories for a service
    pass

@api_view(["DELETE"])
def delete_all_services(request):
    Service.objects.all().delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["GET"])
def list_products(request, service_id):
    service = get_object_or_404(Service, pk=service_id)
    products = service.products.all()
    # Assuming you have a ProductSerializer for serializing products
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)




'''
@api_view(["POST"])
def add_product(request, service_id):
    service = get_object_or_404(Service, pk=service_id)
    product = get_object_or_404(Product, pk=request.data['product'])

    # print(product)
    # print(request.data)
    # print(service.price)
    costSer = 0  # Inicializa cost com um valor padrão

    if request.data.get('measurable') == True:  # Verifica se 'measurable' está presente e é True
        costSer = product.cost * request.data.get('consume', 0)  # Multiplica o custo pelo consumo, usando 0 como padrão se 'consume' não estiver presente
        request.data['cost'] = costSer

        print(costSer)  # Exibe o custo calculado
    else:

        consume_value = request.data.get('consume')
        if consume_value:  # Verifica se 'consume' está presente e não é None ou vazio
            costSer = float(product.cost) / consume_value
            request.data['cost'] = costSer
        else:
            print("Error: 'consume' value is missing or invalid.")


        request.data['cost'] = costSer
        request.data['liquid'] = request.data['business'] - costSer
        request.data['margin'] = float(service.price) - costSer

    print(request.data)

    # print(request.data)
        # adicionar tabela de consumo, a id do produto, estado do produto em uso pendente terminado, data e hora de hoje, 

    serializer = ServiceProductSerializer(data=request.data)
    if serializer.is_valid():
        # Adicione o serviço à instância do ServiceProduct antes de salvar
        serializer.validated_data['service'] = service
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
'''
@api_view(["POST"])
def add_product(request, service_id):
    service = get_object_or_404(Service, pk=service_id)
    request.data['service'] = service.pk
    print(request.data)
    serializer = ServiceProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.validated_data['service'] = service
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["PUT"])
def update_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    serializer = ProductSerializer(product, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def retrieve_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    serializer = ProductSerializer(product)
    return Response(serializer.data)


@api_view(["DELETE"])
def delete_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
