from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def status(request):
    result = {'app':'chatbot service', 'status':'ok', 'version':'0.1'}
    return Response(result)

@api_view(['POST', 'PUT'])
def predict(request):
    result = {'app':'chatbot service', 'status':'ok', 'version':'0.1'}
    return Response(result)