from rest_framework import serializers
from .models import User, product
from django.contrib.auth import authenticate

class UserSerializer (serializers.ModelSerializer):
    class Meta:
        model= User
        fields = ['id', 'username', 'password', 'is_approved', 'is_admin']
        extra_kwargs = {'password':{'write_only': True}}

    def create (self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create_user(**validated_data)
        user.set_password(password)
        user.save()
        return user
        
class LoginSerializer (serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if not user:
            raise serializers.ValidtionError("Invalid Id and Password")
        if not user.is_approved:
            raise serializers.ValidationError("Account not Approved")
        return user
    
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = product
        fields = '__all__'
        read_only_fields = ['owner']
