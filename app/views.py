from django.shortcuts import render,render_to_response,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.template import loader
from django.template.context import RequestContext
from django.core.mail import send_mail
# from dispatch.models import Dispatch_User
import uuid



def index(request):
    index_template = loader.get_template('app/index.html')
    context = {
        "Some random":"Stuf",
    }
    return HttpResponse(index_template.render(context,request))
# Create your views here.
# def login(request):
#     sign_template = loader.get_template('registration/login.html')
#     context ={
#         "loading":"sign_tempalte",
#     }
#     return HttpResponse(sign_template.render(context,request))
#
# def validate(request):
#     if request.method == 'POST':
#         email = request.POST.get('email',None)
#         try:
#             user_name = User.objects.get(email=email).username
#         except User.DoesNotExist:
#             return HttpResponse("User with this email does not exist")
#         password = request.POST.get('password',None)
#         user = authenticate(username=user_name,mail=email,password=password)
#         if user is not None:
#             return HttpResponse("Success")
#         else:
#             return HttpResponse("Failure")
#     else:
#         return HttpResponse("Some random error")
#
# def signup(request):
#     sign_up_template = loader.get_template('registration/registration.html')
#     context = {
#         "loading":"registration",
#     }
#     return HttpResponse(sign_up_template.render(context,request))
#
#
# def save(request):
#     if request.method == 'POST':
#         user_name = request.POST.get("user_name",None)
#         try:
#             uesr_n = User.objects.get(username=user_name)
#             return HttpResponse("Username exists in the database")
#         except User.DoesNotExist:
#             email = request.POST.get("email",None)
#             try:
#                 user_e = User.objects.get(email=email)
#                 return HttpResponse("Email in use")
#             except:
#                 first_name = request.POST.get('first_name',None)
#                 last_name = request.POST.get('last_name',None)
#                 password = request.POST.get('password',None)
#                 new_user = User(username=user_name,password=password,\
#                                 email=email,first_name=first_name,\
#                                 last_name=last_name)
#
#                 new_user.user = request.user
#                 new_user.save()
#                 message = "Thank you for registering with dispatch.\nPlease follow the link to confirm your account."
#                 html = "<a href=http://localhost:8000/dispatch/%s/>http://localhost:8000/dispatch/%s/</a>"%(user_name,user_name)
#                 if send_mail("Dispatch- Please verify your email",message,"dispatchnoreply@gmail.com",["%s"%email],fail_silently=False,html_message=html)==1:
#                     return HttpResponse("Please Wait ")
#                 else:
#                     return HttpResponse("Server Encountered Unexpected error")
#
#
#
# def confirm_email(request,username):
#     try:
#         _id = User.objects.get(username=username).id
#     except User.DoesNotExist:
#         return HttpResponse("Could not confirm your email")
#     try:
#         dispatch_update = Dispatch(user_id=_id,is_verified=True)
#         dispatch_update.save()
#         return redirect('/dispatch/')
#     except:
#         return HttpResponse("Validation Error")
