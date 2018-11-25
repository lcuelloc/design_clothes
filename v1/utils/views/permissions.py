from rest_framework import permissions


class IsClientPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.customer:
            return True
        return False
