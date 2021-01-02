from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import UserAccountManager

User = get_user_model()

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'name','id']

class registrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError(
                {'password': 'Paswords must match'})
        account = User.objects.create_user(email=self.validated_data['email'], name=self.validated_data['name'], password=self.validated_data['password'])
        account.save()
        return account


class LoginSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = '__all__'
        
    email = serializers.EmailField()
    password = serializers.CharField()
