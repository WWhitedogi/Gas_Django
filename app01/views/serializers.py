from rest_framework import serializers
from app01.models import Measurement


class MeasurementSerializer(serializers.ModelSerializer):
    id = id = serializers.IntegerField()
    time = serializers.CharField(max_length=18)
    methane_ppm = serializers.FloatField()
    formaldehyde_ppm = serializers.FloatField()
    temperature = serializers.FloatField()

    class Meta:
        model = Measurement
        fields = '__all__'
