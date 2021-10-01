from django.shortcuts import render
from rest_framework import viewsets, filters
from .models import Daily
from rest_framework.response import Response
from .serializers import DailySerializer
from rest_framework.views import APIView


class DailyViewSet(viewsets.ModelViewSet):
    queryset = Daily.objects.all().order_by('-created_at')
    serializer_class = DailySerializer


class CategoryAPI(APIView):
    serializer_class = DailySerializer

    def get(self, request, category):
        daily = Daily.objects.values_list('created_at', category).order_by('-created_at')
        category_list = {}
        res_list = [
            {
                'date': format(d[0], "%Y-%m-%d"),
                'content': d[1],
            }
            for d in daily
        ]
        category_list['category'] = category
        category_list['data'] = res_list
        return Response(category_list)