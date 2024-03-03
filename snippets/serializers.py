from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES

# 1 versao mostrando o uso de serializer
# class SnippetSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(required=False, allow_blank=True, max_length=100)
#     code = serializers.CharField(style={'base_template': 'textarea.html'})
#     linenos = serializers.BooleanField(required=False)
#     language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default="Python")
#     style = serializers.ChoiceField(choices=STYLE_CHOICES, default='frindly')

#     def create(self, validated_data):
#         # Cria e retorn uma instacia nova de Snippet
#         return Snippet.objects.create(**validated_data)
    

#     def update(self, instance, validated_data):
#         # Atualiza e retorna uma instancia de snippet     
#         instance.title = validated_data.get('title', instance.title)
#         instance.code = validated_data.get('code', instance.code)
#         instance.linenos = validated_data.get('linenos', instance.linenos)
#         instance.language = validated_data.get('linenos', instance.language)
#         instance.style = validated_data.get('style', instance.style)
#         instance.save()

#         return super().update(instance, validated_data)


# É importante lembrar que ModelSerializeras classes não fazem nada particularmente mágico, elas são simplesmente um atalho para criar classes serializadoras:

# Um conjunto de campos determinado automaticamente.
# Implementações padrão simples para os métodos create()e update().
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())
    class Meta:
        model = User 
        fields = ['id', 'username', 'snippts']




class SnippetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Snippet
        fields = ['owner','id', 'title', 'code', 'linenos', 'language', 'style']
