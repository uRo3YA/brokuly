# from django.conf import settings
# from django.shortcuts import redirect
# from django.contrib import messages

# # from .models import User
# from accounts.models import User
# from django.http import HttpResponse


# def seller_required(function):
#     def wrap(request, *args, **kwargs):
#         if request.user.is_seller:
#             return function(request, *args, **kwargs)

#         messages.info(request, "접근 권한이 없습니다.")
#         return redirect("/")

#     return wrap
