from rest_framework.permissions import BasePermission


class IsRegionalManager(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'regional_manager'

class IsPresident(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'president'

class IsDeliveryPersonel(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'delivery_personel'
    
class IsRegionalManagerOrPresident(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'regional_manager' or request.user.role == "president"