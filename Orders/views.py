from rest_framework import viewsets, filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from .models import Order
from .serializers import OrderSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().order_by('-created_at')
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    # Фильтрация и поиск
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['client', 'project_name']  # Поиск по клиенту и названию проекта
    ordering_fields = ['created_at', 'deadline']  # Сортировка по дате создания и дедлайну

    def perform_create(self, serializer):
        # Сохраняем данные и связываем с текущим пользователем
        serializer.save(client=self.request.user)
