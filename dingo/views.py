from django.contrib.auth import logout
from django.shortcuts import redirect
def logout_view(request):
    print("LOGOUT VIEW CALLED")
    logout(request)
    next_url = request.META.get('HTTP_REFERER', '/')
    return redirect(next_url)