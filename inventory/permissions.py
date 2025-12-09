from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsProductOwnerOrReadOnly(BasePermission):
    """Anyone can view, but only owners can update the inventory"""
    

    def has_object_permission(self, request, view, obj):
        # SAFE METHODS → allow everyone to read
        if request.method in SAFE_METHODS:
            return True
        
        # Write permissions → only product owners
        return obj.product.owner == request.user
