from rest_framework import permissions

class IsOwner(permissions.BasePermission):
   def has_object_permission(self, request, view, obj):
      return obj.user == request.user


class IsAdminUserOrReadOnly(permissions.IsAdminUser):
   def has_permission(self, request, view):
      is_admin = super(
         IsAdminUserOrReadOnly, 
         self).has_permission(request, view)
      return request.method in permissions.SAFE_METHODS or is_admin
