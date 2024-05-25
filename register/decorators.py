from django.shortcuts import redirect

def notLogUser(func_view):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return func_view(request, *args, **kwargs)  
    return wrapper_func
                
def allowedUsers(view_func):
    def wrapper_func(request, *args, **kwargs):
        groups = request.user.groups.values_list('name', flat=True) 
        if 'admin' in groups:
            return view_func(request, *args, **kwargs)
        if 'students' in groups:
            return redirect('profile')
        return redirect('some_other_view') 
    return wrapper_func