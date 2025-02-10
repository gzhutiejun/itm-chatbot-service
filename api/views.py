from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def getStatus(request):
    status = {'app':'chatbot service', 'status':'ok', 'version':'0.1'}
    return Response(status)