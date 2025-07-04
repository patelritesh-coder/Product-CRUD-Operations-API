from django.urls import path
from .views import RegisterView, LoginView, ProductListCreate, ProductRetrieveUpdateDelete

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('products/', ProductListCreate.as_view()),
    path('products/<int:pk>/', ProductRetrieveUpdateDelete.as_view())

]