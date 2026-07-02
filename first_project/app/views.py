from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def app(request):
    data = {'mes':'ПИДАРАС'}
    return Response(data)


