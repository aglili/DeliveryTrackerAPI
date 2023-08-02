from .serializer import UserSignUpSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response



@api_view(['POST'])
def createNewUser(request):
    serializer = UserSignUpSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response({
            "status": "True",
            "message": "User Has Been Created",
            "data": serializer.data
        },status=status.HTTP_201_CREATED)