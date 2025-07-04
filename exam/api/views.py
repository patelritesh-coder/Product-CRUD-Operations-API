from rest_framework import generics, permissions, status
from .models import User, product
from .serializers import UserSerializer, LoginSerializer, ProductSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data= request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        token,_ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})

class ProductListCreate(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_admin:
            return product.objects.all()

        return product.objects.filter(owner=user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ProductRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = product.objects.all()
