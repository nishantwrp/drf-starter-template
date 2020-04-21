from rest_framework import permissions

# Sample Permission

# class AllowValidUser(permissions.BasePermission):
#     message = "You need to register first"

#     def has_permission(self,request,view):
#         profile = Profile.objects.filter(user=request.user)
#         if profile:
#             return True
#         else:
#             return False
