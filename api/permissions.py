from rest_framework import permissions


class IsOwnerObj(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ('PUT', 'PATCH', 'DELETE'):
            return obj.author == request.user
        elif request.method == 'POST':
            return request.user.is_authenticated
        return True
