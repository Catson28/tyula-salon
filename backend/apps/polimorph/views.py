# views.py

from rest_framework import generics, status
from rest_framework.response import Response
from .models import Comentario, Foto
from .serializers import ComentarioSerializer, FotoSerializer
from django.contrib.contenttypes.models import ContentType


from .models import Funcionario
from .serializers import FuncionarioSerializer

class ComentarioListCreate(generics.ListCreateAPIView):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(autor=request.user)  # Defina o autor conforme sua lógica de autenticação
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

'''
class FotoListCreate(generics.ListCreateAPIView):
    queryset = Foto.objects.all()
    serializer_class = FotoSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(autor=request.user)  # Defina o autor conforme sua lógica de autenticação
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FotoListCreate(generics.ListCreateAPIView):
    queryset = Foto.objects.all()
    serializer_class = FotoSerializer

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            request_data = request.data.copy()  # Cria uma cópia mutável dos dados da solicitação
            request_data['autor'] = request.user.id  # Define o autor como o usuário autenticado
            serializer = self.get_serializer(data=request_data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"error": "Usuário não autenticado"}, status=status.HTTP_401_UNAUTHORIZED)

'''


class FuncionarioCreate(generics.CreateAPIView):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# from rest_framework import generics, status
# from rest_framework.response import Response
# from .models import Foto
# from .serializers import FotoSerializer


'''
class FotoListCreate(generics.ListCreateAPIView):
    queryset = Foto.objects.all()
    serializer_class = FotoSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            # Defina o autor da foto conforme sua lógica de autenticação
            # Aqui estou supondo que você deseja definir o autor como o usuário autenticado
            serializer.save(autor=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FotoListCreate(generics.ListCreateAPIView):
    queryset = Foto.objects.all()
    serializer_class = FotoSerializer

    def post(self, request, *args, **kwargs):
        data = {
            'url': request.data.get('url'),
            'content_type': request.data.get('content_type'),
            'object_id': request.data.get('object_id')
        }
        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            # Verifica se o Funcionario com o ID fornecido na requisição existe
            funcionario_id = request.data.get('object_id')
            if Funcionario.objects.filter(pk=funcionario_id).exists():
                serializer.save(autor_id=funcionario_id)  # Define o autor como o funcionário correspondente
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response({"error": "Funcionario não encontrado"}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


'''




class FotoListCreate(generics.ListCreateAPIView):
    queryset = Foto.objects.all()
    serializer_class = FotoSerializer

    def post(self, request, *args, **kwargs):
        url = request.data.get('url')
        content_type_str = request.data.get('content_type')
        object_id = request.data.get('object_id')
        autor = request.data.get('autor')
        
        # Verifica se o Funcionario com o ID fornecido na requisição existe
        try:
            content_type = ContentType.objects.get(model=content_type_str)
        except ContentType.DoesNotExist:
            return Response({"error": f"Tipo de conteúdo '{content_type_str}' não encontrado."},
                            status=status.HTTP_404_NOT_FOUND)
        
        data = {
            'url': url,
            'content_type': content_type.id,
            'object_id': object_id,
            'autor': autor
        }
        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            serializer.save(autor_id=object_id)  # Define o autor como o funcionário correspondente
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
