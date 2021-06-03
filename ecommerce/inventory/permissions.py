from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Allow read access to any user, 
    Allow create, destroy, update access only to Admin users.
    """

    def has_permission(self, request, view):
        
        if request.user.is_authenticated and request.user.is_superuser:
            return True
        
        return request.method in permissions.SAFE_METHODS
           
        



