from rest_framework import serializers
from . models import Store
from accounts.models import CustomUser




class CreateStoreSerializer(serializers.ModelSerializer):

    store_id = serializers.CharField(required=False)
    class Meta:
        model = Store
        fields = ["store_id","city","region","phone_number","email","manager","created_at","ghp_address"]


    manager = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all(),required=False,allow_null =True)

    def validate_manager(self,value):

        user = self.context["request"].user

        if not user or user.role != "manager":
            raise serializers.ValidationError("Not Qualified")
        
        return value
    
    def create(self,validated_data):
        manager = validated_data.get("manager",None)

        store = Store.objects.create(
            city=validated_data['city'],
            region=validated_data['region'],
            phone_number=validated_data['phone_number'],
            email=validated_data['email'],
            manager=manager
        )
        store.save()


        return store



class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ["city", "region", "phone_number", "email", "manager_email","manager_phone_number","ghp_address"]

    manager_email = serializers.SerializerMethodField()
    manager_phone_number = serializers.SerializerMethodField()

    def get_manager_email(self,obj):
        return obj.manager.email if obj.manager else None
    
    def get_manager_phone_number(self,obj):
        return obj.manager.phone_number if obj.manager else None
    




    