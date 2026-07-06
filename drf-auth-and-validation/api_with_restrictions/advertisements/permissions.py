from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Разрешение на редактирование объекта только его автору.
    """

    def has_object_permission(self, request, view, obj):
        # Разрешаем безопасные методы (GET, HEAD, OPTIONS) любому
        if request.method in permissions.SAFE_METHODS:
            return True

        # Запись (PUT/PATCH/DELETE) только автору
        return obj.author == request.user