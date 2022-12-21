from django.views.generic import DetailView
from rest_framework.response import Response

from .models import DrinkModel
from .serializers import DrinkSerializer
from rest_framework import generics, status


# lists all drinks in db
class DrinkListView(generics.ListAPIView):
    queryset = DrinkModel.objects.all()
    serializer_class = DrinkSerializer


# # create a drink
class DrinkCreateView(generics.CreateAPIView):
    queryset = DrinkModel.objects.all()
    serializer_class = DrinkSerializer


# get specific drink details
class DrinkDetailView(DetailView):
    model = DrinkModel
    template_name = 'model_detail.html'


# delete specific drink
class DrinkDeleteView(generics.DestroyAPIView):
    queryset = DrinkModel.objects.all()
    serializer_class = DrinkSerializer
