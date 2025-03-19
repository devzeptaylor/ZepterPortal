from django.contrib.auth.models import User
from django.db import models
from django.db import connections


# Create your models here.
class Telefon(models.Model):
    fio = models.CharField(max_length=255)
    tel = models.CharField(max_length=25)
    mobile = models.CharField(max_length=25)
    user = models.ForeignKey(User,on_delete=models.SET_NULL, null=True)


# Пример создания модели для работы со второй базой данных
class OracleData(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)

    class Meta:
        managed = False  # Не будет использоваться миграции
        db_table = 'temp_04_10 '
        app_label = 'contacts'

# Пример запроса данных из второй базы данных (Oracle)
def get_oracle_data():
    # Выполнение запроса через второй источник данных
    oracle_data = OracleData.objects.using('oracle_db').all()
    for data in oracle_data:
        print(data.id, data.name)
    return oracle_data
