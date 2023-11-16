from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from app01.views.serializers import MeasurementSerializer
from ..models import Measurement


class measurement(APIView):
    def get(self, request, id=None):
        if id:
            read = Measurement.objects.get(id=id)
            serializer = MeasurementSerializer(read)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        readings = Measurement.objects.all()
        serializer = MeasurementSerializer(readings, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
