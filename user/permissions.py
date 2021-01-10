from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object edit it.
    """
    def has_object_permission(self, request, view, obj):
        return obj.id == request.user.id