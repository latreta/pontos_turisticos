from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from atracoes.api.serializers import AtracaoSerializer
from core.models import PontoTuristico
from enderecos.api.serializers import EnderecoSerializer


class PontoTuristicoSerializer(ModelSerializer):
    descricao_completa = SerializerMethodField()
    atracoes = AtracaoSerializer(many=True, read_only=True)
    endereco = EnderecoSerializer(many=False, read_only=True)

    class Meta:
        model = PontoTuristico
        fields = ('id', 'nome', 'descricao_completa', 'descricao_completa2', 'aprovado', 'foto', 'endereco', 'atracoes')

    def get_descricao_completa(self, obj):
        return '%s - %s' % ('Descricao', obj.descricao)
