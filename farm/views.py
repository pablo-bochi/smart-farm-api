from rest_framework.views import APIView
from rest_framework.response import Response
from .tasks import process_sensor_data


class TriggerProcessingView(APIView):
    def post(self, request):
        sensor_id = request.data.get("sensor_id")
        task = process_sensor_data.delay(sensor_id)
        return Response({"task_id": task.id})
