from django.views.generic import DetailView
from rest_framework.response import Response

from .models import DrinkModel
from .serializers import DrinkSerializer
from rest_framework import generics, status


# lists all drinks in db
class DrinkListView(generics.ListAPIView):
    def get_queryset(self):
        drinks = DrinkModel.objects.all()
        serializer = DrinkSerializer(drinks)
        return Response(serializer.data)


# # create a drink
class DrinkCreateView(generics.CreateAPIView):

    def post(self, request, *args, **kwargs):
        serializer_class = DrinkSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data, status=status.HTTP_201_CREATED)
        return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)


# get specific drink details
class DrinkDetailView(DetailView):
    model = DrinkModel
    template_name = 'model_detail.html'
