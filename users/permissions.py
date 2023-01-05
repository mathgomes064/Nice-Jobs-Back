from rest_framework.permissions import BasePermission


class IsOwnerResource(BasePermission):
    edit_methods = ("PUT", "PATCH")

    def has_object_permission(self, request, view, obj):
        if request.method not in self.edit_methods:
            return True

        if "is_premium" in request.data:
            return False

        return request.user == obj
