from django.shortcuts import redirect

def notLogUser(func_view):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return func_view(request, *args, **kwargs)  
    return wrapper_func

# def allowedUsers(allowedGroups=[]):
#     def decorator(view_func):
#         def wrapper_func(request, *args, **kwargs):
#             group=None
#             if request.user.groups.exists():
#                 group=request.user.groups.all()[0].name
#             if group in allowedGroups:
#                 return view_func(request, *args, **kwargs)
#             else:
#                 return redirect('profile/')
#         return wrapper_func
#     return decorator

# def allowedUsers(view_func):
#     def wrapper_func(request, *args, **kwargs):
#         group = None
#         if request.user.groups.exists():  # Check if the user has any groups
#             group = request.user.groups.all()[0].name  # Get the name of the first group
#             if group =='admin':
#                 return view_func(request, *args, **kwargs)  # User is in an allowed group
#             if group =='students':
#                 return redirect('profile')
#     return wrapper_func
                
def allowedUsers(view_func):
    def wrapper_func(request, *args, **kwargs):
        groups = request.user.groups.values_list('name', flat=True) 
        if 'admin' in groups:
            return view_func(request, *args, **kwargs)
        if 'students' in groups:
            return redirect('profile')
        return redirect('some_other_view') 
    return wrapper_func