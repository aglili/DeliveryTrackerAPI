from .serializer import UserSignUpSerializer,UserLoginSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response



@api_view(['POST'])
def registerNewUser(request):
    serializer = UserSignUpSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response({
            "status": "True",
            "message": "User Has Been Created",
            "data": serializer.data
        },status=status.HTTP_201_CREATED)
    
@api_view(['POST'])
def userLogin(request):
    serializer = UserLoginSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        token_data = serializer.create_token(serializer.validated_data)
        return Response(
            {
                "status":True,
                "message":"Login Succesful",
                "keys": token_data   
            }
        )
            
