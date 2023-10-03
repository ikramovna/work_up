from rest_framework.serializers import ModelSerializer



class ColumnModelSerializer(ModelSerializer):
    class Meta:
        model = Column
        fields = ('id', 'name', 'board_id')
