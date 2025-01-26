from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')
        read_only_fields = ('id',)

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2')
        extra_kwargs = {'password': {'write_only': True}}
        
    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError("Passwords don't match")
        return data
    def create(self, validated_data):
        validated_data.pop('password2')  # Remove password2 from the data
        password = validated_data.pop('password')
        
        # Create user using UserManager's create_user method
        user = User.objects.create_user(
            password=password,
            **validated_data
        )
        return user

class LoginSerializer(serializers.Serializer):
        username = serializers.CharField(label='Username or Email')
        password = serializers.CharField(write_only=True)

        def validate(self, data):
            username = data.get('username')
            password = data.get('password')
            
            if username and password:
                # Try to authenticate with username/email
                user = authenticate(
                    request=self.context.get('request'),
                    username=username,
                    password=password
                )
                
                if not user:
                    msg = 'Unable to log in with provided credentials.'
                    raise serializers.ValidationError(msg, code='authorization')
            else:
                msg = 'Must include "username" and "password".'
                raise serializers.ValidationError(msg, code='authorization')

            data['user'] = user
            return data

class PasswordChangeSerializer(serializers.Serializer):
        old_password = serializers.CharField(required=True)
        new_password = serializers.CharField(required=True)
        confirm_password = serializers.CharField(required=True)

        def validate(self, data):
            if data['new_password'] != data['confirm_password']:
                raise serializers.ValidationError("New passwords don't match")
            return data