from rest_framework.serializers import ModelSerializer

from conatcts.models import Telefon, OracleData


class TelefonSerializer(ModelSerializer):
    class Meta:
        model = Telefon
        fields = ['fio','tel']


class OracleDataSerializer(ModelSerializer):
    class Meta:
        model = OracleData
        fields = ['saradnik#','transfer_date']