from django.shortcuts import render
from rest_framework import viewsets

from .models import Company
from .serializers import CompanySerializer


def index(request):
    return render(request, 'main/index.html')


class CompanyViewSet(viewsets.ModelViewSet):

    queryset = Company.objects.all()
    serializer_class = CompanySerializer
