from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from core.api.serializers import PontoTuristicoSerializer
from core.models import PontoTuristico


class PontoTuristicoViewSet(ModelViewSet):
    serializer_class = PontoTuristicoSerializer
    # permission_classes = (IsAuthenticated,)
    authentication_classes = {TokenAuthentication}
    filter_backends = {SearchFilter, OrderingFilter}
    search_fields = {'nome', 'descricao', '^endereco__rua'}
    ordering_fields = ['nome']

    def get_queryset(self):
        id = self.request.query_params.get('id', None)
        nome = self.request.query_params.get('nome', None)
        descricao = self.request.query_params.get('descricao', None)
        queryset = PontoTuristico.objects.all()
        if id:
            queryset = queryset.filter(pk=id)
        if nome:
            queryset = queryset.filter(nome__iexact=nome)
        if descricao:
            queryset = queryset.filter(descricao__iexact=descricao)

        return queryset

    @action(methods=['GET'], detail=False)
    def denunciar(self, request):
        return Response({"Response": "Denunciado com sucesso"})
