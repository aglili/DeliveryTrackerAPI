from .models import CustomUser
from rest_framework import serializers
from .utils import validate_ghanaian_phone_number
from .errors import InvalidNumber




class UserSignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username','password','phone_number']

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
