# serializers.py

from rest_framework import serializers
from .models import Comentario, Foto, Funcionario
from django.contrib.contenttypes.models import ContentType


class FuncionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcionario
        fields = ['id', 'nome', 'cargo']

'''
class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = ['id', 'conteudo', 'content_type', 'object_id', 'autor']
'''

class ComentarioSerializer(serializers.ModelSerializer):
    content_type = serializers.CharField(write_only=True)
    object_id = serializers.IntegerField(write_only=True)
    autor = FuncionarioSerializer(read_only=True)

    class Meta:
        model = Comentario
        fields = ['id', 'conteudo', 'content_type', 'object_id', 'autor']

    def create(self, validated_data):
        content_type = validated_data.pop('content_type')
        object_id = validated_data.pop('object_id')
        comentario = Comentario.objects.create(**validated_data)
        comentario.content_type = ContentType.objects.get_for_model(self.Meta.model)
        comentario.object_id = object_id
        comentario.save()
        return comentario


'''
class FotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Foto
        fields = ['id', 'url', 'content_type', 'object_id', 'autor']
'''
class FotoSerializer(serializers.ModelSerializer):
    content_type = serializers.CharField(write_only=True)
    object_id = serializers.IntegerField(write_only=True)
    autor = FuncionarioSerializer(read_only=True)

    class Meta:
        model = Foto
        fields = ['id', 'url', 'content_type', 'object_id', 'autor']

    def create(self, validated_data):
        content_type = validated_data.pop('content_type')
        object_id = validated_data.pop('object_id')
        foto = Foto.objects.create(**validated_data)
        foto.content_type = ContentType.objects.get_for_model(self.Meta.model)
        foto.object_id = object_id
        foto.save()
        return foto
