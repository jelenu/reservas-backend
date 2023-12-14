from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status,  generics, permissions
from datetime import datetime
from django.db.models import Q
from .models import VehicleModel, Office
from .serializers import AvailableModelsSerializer, VehicleModelSerializer, OfficeSerializer
from django.db.models import Q
from Booking.models import Booking

class VehicleListView(generics.ListAPIView):
    queryset = VehicleModel.objects.all()
    serializer_class = VehicleModelSerializer
    permission_classes = [permissions.AllowAny]

class OfficeListView(generics.ListAPIView):
    queryset = Office.objects.all()
    serializer_class = OfficeSerializer
    permission_classes = [permissions.AllowAny]



@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def get_available_models(request):
    try:
        # Obtener datos del formulario
        pickup_office_id = request.data.get('pickup_office_id')
        start_date_str = request.data.get('start_date')
        end_date_str = request.data.get('end_date')

        # Validar que ambos campos estén presentes
        if not pickup_office_id or not start_date_str or not end_date_str:
            return Response({'error': 'Se requieren los campos pickup_office_id, start_date y end_date en la solicitud'}, status=status.HTTP_400_BAD_REQUEST)

        # Convertir las fechas a objetos datetime
        start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
        end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()

        # Obtener las reservas que se superponen con el rango de fechas
        overlapping_reservations = Booking.objects.filter(
            Q(start_date__range=(start_date, end_date)) |
            Q(end_date__range=(start_date, end_date)) |
            (Q(start_date__lte=start_date) & Q(end_date__gte=end_date))
        )

        # Obtener los modelos de vehículos de las reservas superpuestas
        reserved_model_ids = overlapping_reservations.values_list('assigned_vehicle__model__id', flat=True)

        # Obtener los modelos de vehículos disponibles en la oficina para el rango de fechas dado
        available_models = VehicleModel.objects.filter(
            ~Q(id__in=reserved_model_ids),
            vehicle__location_id=pickup_office_id
        )

        serialized_models = AvailableModelsSerializer(available_models, many=True, context={'request': request}).data

        return Response(serialized_models, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

