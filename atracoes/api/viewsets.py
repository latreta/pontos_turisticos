from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet
from atracoes.api.serializers import AtracaoSerializer
from atracoes.models import Atracao


class AtracaoViewSet(ModelViewSet):
    queryset = Atracao.objects.all()
    serializer_class = AtracaoSerializer
    filter_backends = {SearchFilter, OrderingFilter}
    filter_fields = {'nome', 'descricao'}
    ordering_fields = ['nome']
