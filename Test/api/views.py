from rest_framework.response import Response
from rest_framework.decorators import api_view
from Profile.models import Profile
from .serializers import Profileserializer


@api_view (['GET'])
def getdata (request):
    profiles = Profile.objects.all()
    serializer = Profileserializer(profiles, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def addProfile (request):
    serializer = Profileserializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


