from .models import CustomUser
from rest_framework import serializers
from .utils import validate_ghanaian_phone_number
from .errors import InvalidNumber
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken




class UserSignUpSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=True,write_only=True)
    class Meta:
        model = CustomUser
        fields = ['username','password','phone_number','role']

    def validate(self, attrs):
        phone_number = attrs.get("phone_number")

        validated_number = validate_ghanaian_phone_number(phone_number)

        if not validated_number:
            raise InvalidNumber("The Number Is Incorrect, Try Again")
        
        return attrs
    
    def create(self, validated_data):
        user = CustomUser.objects.create(
            username = validated_data['username'],
            phone_number=validated_data['phone_number'],
            role = validated_data['role']   
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True,write_only=True)

    def validate(self, attrs):
        if not CustomUser.objects.filter(username=attrs["username"]):
            raise serializers.ValidationError("User Does Not Exist!")
        return attrs
    
    def create_token(self,attrs):
        user = authenticate(username=attrs["username"],password=attrs["password"])
        if not user:
            raise serializers.ValidationError("Invalid Credentials")
        
        refresh = RefreshToken.for_user(user)

        
        token_data = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

        print(user)

        user_data = {
            "user_id":user.id,
            "username":user.username
        }

        token_data["user"] = user_data

        return token_data
    

        

