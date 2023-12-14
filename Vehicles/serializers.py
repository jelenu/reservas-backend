from rest_framework import serializers
from .models import VehicleModel, Office

class VehicleModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleModel
        fields = '__all__'

class OfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Office
        fields = '__all__'

class AvailableModelsSerializer(serializers.ModelSerializer):
    # Incluir la URL completa de la imagen
    image = serializers.SerializerMethodField()

    class Meta:
        model = VehicleModel
        fields = '__all__'

    def get_image(self, obj):
        # Devolver la URL completa de la imagen
        if obj.image:
            return self.context['request'].build_absolute_uri(obj.image.url)
        return None