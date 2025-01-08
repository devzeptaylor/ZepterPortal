from rest_framework.serializers import ModelSerializer

from conatcts.models import Telefon


class TelefonSerializer(ModelSerializer):
    class Meta:
        model = Telefon
        fields = ['fio','tel']