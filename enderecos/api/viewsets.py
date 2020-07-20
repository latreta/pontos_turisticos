from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.state import User
from rolepermissions.checkers import has_permission
from rolepermissions.roles import assign_role

from enderecos.api.serializers import EnderecoSerializer
from enderecos.models import Endereco


class EnderecoViewSet(ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer
