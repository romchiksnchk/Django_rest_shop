from rest_framework import permissions


class IsUserUpdate(permissions.BasePermission):
    """Проверка для изменения пользователя"""
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.is_staff or request.user.is_authenticated and obj.id == request.user.id


class IsUserOwner(permissions.BasePermission):
    """Проверка на владение обьектом"""

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.is_staff or request.user.is_authenticated and obj.user == request.user
