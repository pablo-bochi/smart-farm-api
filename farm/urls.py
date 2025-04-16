from django.urls import path
from .views import TriggerProcessingView

urlpatterns = [
    path('process/', TriggerProcessingView.as_view()),
]
