from rest_framework import permissions


class IsAdminUserOrReadOnly(permissions.IsAdminUser):
    def has_permission(self, request, view):
        # print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        is_admin = super().has_permission(request, view)
        """ここでユーザーがスーパーユーザなのかそうでないかを判断している"""
        """スーパーユーザーならTrueそれ以外ならFalse"""
        # print("#################################")
        # print(is_admin)
        # print(permissions.SAFE_METHODS)
        # print("#################################")
        return request.method in permissions.SAFE_METHODS or is_admin


class IsReviewAuthOrReadOnly(permissions.BasePermission):
    def has_object_permission(self,review,view,obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.review_author == request.user