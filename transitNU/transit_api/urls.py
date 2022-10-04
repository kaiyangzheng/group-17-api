from django.urls import path
from .views import TrainList

urlpatterns = [
    path('train/', TrainList.as_view(), name="train-list")
]