from django.shortcuts import render
from django.shortcuts import redirect

from rest_framework.decorators import api_view,parser_classes
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from rest_framework import status

from .serializers import ProfileSerializer
# Create your viewss= here.


def redirect_to_3000(request, uid, token):
    print('http://localhost:3000/activate/'+uid+'/'+token)
    return redirect('http://localhost:3000/activate')

@api_view(['POST'])
@parser_classes([MultiPartParser])
def create_profile(request, format=None):
    data = request.data
    serializer = ProfileSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
