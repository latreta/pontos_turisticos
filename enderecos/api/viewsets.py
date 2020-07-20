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

    def list(self, request, *args, **kwargs):
        user = User.objects.get(id=1)
        assign_role(user, 'doctor')
        return HttpResponse(has_permission(user, 'create_medical_record'))
