from celery import shared_task
import time


@shared_task
def process_sensor_data(sensor_id):
    time.sleep(5)
    return f"Sensor {sensor_id} processed"
