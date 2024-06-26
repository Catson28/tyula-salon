from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Image, ServiceImage, CategoryImage, ProductImage
from .serializers import ImageSerializer, ServiceImageSerializer, ProductSerializer
from django.contrib.contenttypes.models import ContentType
from apps.product.models import Product
from apps.category.models import Category
from apps.service.models import Service
from rest_framework.views import APIView

"""
@api_view(['POST'])
def add_image(request):
    serializer = ImageSerializer(data=request.data)
    print(request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)
@api_view(['POST'])
def add_image(request):
    serializer = ImageSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

"""


@api_view(["POST"])
def add_image(request):
    # Verifique se a solicitação é do tipo POST
    if request.method == "POST":
        # Verifique se os dados fornecidos são válidos usando o ImageSerializer
        serializer = ImageSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            # Obtenha o ID do produto fornecido nos dados da solicitação
            product_id = serializer.validated_data.get("product")
            # Obtenha o objeto Product correspondente ao ID fornecido
            product = get_object_or_404(Product, pk=product_id)

            # Obtém o tipo de conteúdo (ContentType) para o modelo Product
            product_content_type = ContentType.objects.get_for_model(Product)

            # Cria uma nova instância de Imagem relacionada ao Produto
            serializer.save(content_type=product_content_type, object_id=1)
            return Response(serializer.data, status=201)
        # Se os dados fornecidos não forem válidos, retorne os erros
        return Response(serializer.errors, status=400)
    # Se a solicitação não for do tipo POST, retorne uma resposta de erro
    return Response({"erro": "Método não permitido"}, status=405)


'''
@api_view(["POST"])
def UploadCategoryImageView(request):
        serializer = ImageSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            image = serializer.save()
            
            # Supondo que o ID da categoria seja passado no corpo da requisição
            category_id = request.data.get('category_id')
            category = Category.objects.get(pk=category_id)
            
            # Criando a relação entre a imagem e a categoria
            CategoryImage.objects.create(category=category, image=image)
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
'''

@api_view(["POST"])
def UploadCategoryImageView(request):
    serializer = ImageSerializer(data=request.data)
    if serializer.is_valid():
        image = serializer.save()
        
        # Verifique se o ID da categoria foi fornecido na requisição
        category_id = request.data.get('category_id')
        if category_id is not None:
            # Tente obter a categoria com o ID fornecido
            category = get_object_or_404(Category, pk=category_id)
            
            # Criando a relação entre a imagem e a categoria
            CategoryImage.objects.create(category=category, image=image)
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            # Caso não tenha sido fornecido um ID de categoria, retorne um erro
            return Response({"error": "Category ID is required"}, status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def UploadServiceImageView(request):
    serializer = ImageSerializer(data=request.data)
    print(request.data)
    if serializer.is_valid():
        image = serializer.save()
        service_id = request.data.get('service_id')
        if service_id is not None:
            service = get_object_or_404(Service, pk=service_id)
            if request.data.get('cover', False):
                cover = True
            else:
                cover = False
            # print(cover)
            ServiceImage.objects.create(service=service, image=image, cover=cover)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"error": "Service ID is required"}, status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
def UploadProductImageView(request):
    serializer = ImageSerializer(data=request.data)
    if serializer.is_valid():
        image = serializer.save()
        product_id = request.data.get('product_id')
        if product_id is not None:
            product = get_object_or_404(Product, pk=product_id)
            if request.data.get('cover', False):
                cover = True
            else:
                cover = False
            ProductImage.objects.create(product=product, image=image, cover=cover)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"error": "Product ID is required"}, status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(["GET"])
def view_image(request, image_id):
    image = get_object_or_404(Image, pk=image_id)
    serializer = ImageSerializer(image)
    return Response(serializer.data)


@api_view(["DELETE"])
def delete_image(request, image_id):
    image = get_object_or_404(Image, pk=image_id)
    image.delete()
    return Response(status=204)


@api_view(["POST"])
def associate_image_with_service(request):
    serializer = ServiceImageSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(["POST"])
def associate_image_with_raw_material(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(["GET"])
def list_images_by_type(request):
    images = Image.objects.all()
    serializer = ImageSerializer(images, many=True)
    return Response(serializer.data)


@api_view(["PUT"])
def update_image_description(request, image_id):
    image = get_object_or_404(Image, pk=image_id)
    serializer = ImageSerializer(image, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)
