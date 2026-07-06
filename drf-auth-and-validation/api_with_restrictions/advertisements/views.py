from rest_framework import viewsets, status, serializers
from rest_framework.response import Response
from django.db.models import Count
from .models import Advertisement
from .serializers import AdvertisementSerializer
from .filters import AdvertisementFilter
from .permissions import IsAuthorOrReadOnly


class AdvertisementViewSet(viewsets.ModelViewSet):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filterset_class = AdvertisementFilter
    permission_classes = [IsAuthorOrReadOnly]  # важно: применяем к каждому объекту

    def get_permissions(self):
        """
        Для создания требуется авторизация, для просмотра — нет.
        """
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            # Можно оставить IsAuthorOrReadOnly, но для create нужен просто IsAuthenticated
            from rest_framework.permissions import IsAuthenticated
            return [IsAuthenticated()]
        return super().get_permissions()

    def perform_create(self, serializer):
        """
        Принудительно ставим автора из request.user, чтобы нельзя было подменить.
        Это критично для безопасности.
        """
        user = self.request.user
        open_count = Advertisement.objects.filter(author=user, status='OPEN').count()
        if open_count >= 10:
            raise serializers.ValidationError({'status': 'У вас уже 10 открытых объявлений.'})
        serializer.save(author=user)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        # Дополнительная проверка на всякий случай (хотя permission её уже делает)
        if instance.author != request.user:
            return Response({'detail': 'Вы не можете удалять чужие объявления'}, status=status.HTTP_403_FORBIDDEN)
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

