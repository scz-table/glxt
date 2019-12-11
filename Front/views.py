from django.http import HttpResponse
from django.shortcuts import redirect,reverse,render
from django.views.generic import View
from django.views.decorators.http import require_GET,require_http_methods,require_POST
from .models import *
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required,permission_required
from django.contrib.auth.models import Permission,ContentType,Group
# from django.contrib import messages
from Universalscript import errorTips,generalVar
from Department.models import Department,Position
from django.views.decorators.csrf import csrf_exempt

def index(request):
    return render(request,'Front/index.html')

def console(request):
    return render(request,'pages/console.html')
def console1(request):
    return render(request,'pages/console1.html')


@login_required
def test(request):
    if request.method == 'GET':
        context={
            'table_count':range(30)
        }
        return render(request, 'Front/test.html',context=context)
    if request.method == 'POST':
        pass

# class signin(View):
#     def get(self,request,*args,**kwargs):
#         form = SigninForm(self.request.POST)
#         return render(request,generalVar.signin_url,{'obj':form})
#     def post(self,request):
#         form = SigninForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             remember = form.cleaned_data.get('remember')
#             print('您输入的信息：',username,password,remember)
#             user = authenticate(request, username=username, password=password)
#             print('user:',user)
#             # user=my_authenticate(username=username,password=password)
#             if user and user.is_active:
#                 login(request, user)
#                 if remember:
#                     request.session.set_expiry(None)
#                 else:
#                     request.session.set_expiry(0)
#                 next_url = request.GET.get('next')
#                 if next_url:
#                     return redirect(next_url)
#                 else:
#                     return redirect(reverse('front:front_index'))
#             else:
#                 request.META['check_login_errors'] = {
#                     'username': [
#                         ('验证错误：','您的用户名或者密码输入错误！')
#                     ]
#                 }
#                 return render(request, generalVar.signin_url,{'obj':form})
#         else:
#             request.META['check_login_errors'] = form.get_error()
#             return render(request, generalVar.signin_url,{'obj':form})

@require_http_methods(["GET","POST"])
@csrf_exempt
def signin(request):
    form = SigninForm(request.POST)
    myuser=request.user
    remember = request.POST.get('remember')
    next_url = request.GET.get('next')

    if request.method == 'POST':
        form = SigninForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            # print('您输入的信息：',username,password,remember)
            myuser = authenticate(request, username=username, password=password)
            # print('user:',user)
            # user=my_authenticate(username=username,password=password)
            if myuser and myuser.is_active:
                login(request, myuser)
                if remember:
                    request.session.set_expiry(None)
                else:
                    request.session.set_expiry(0)
                print("登录成功！")
                if next_url:
                    return HttpResponse(next_url)
                else:
                    return HttpResponse(reverse('front:front_index'))
            else:
                request.META['check_login_errors'] = {
                    'username': [
                        ('验证错误：','您的用户名或者密码输入错误！')
                    ]
                }
        else:
            request.META['check_login_errors'] = form.get_error()

    if myuser and myuser.is_active and next_url:
        return redirect(reverse('front:front_index'))
    else:
        return render(request,generalVar.signin_url,{'obj':form})

@require_http_methods(["GET","POST"])
@csrf_exempt
def signup(request):
    form = SignupForm(request.POST)
    User_Extension_Form = User_Extension_Signup_Form(request.POST)

    if request.method == 'POST':
        if form.is_valid()*User_Extension_Form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            email = form.cleaned_data.get('email')
            telephone = User_Extension_Form.cleaned_data.get('telephone')
            phone = User_Extension_Form.cleaned_data.get('phone')
            fullname = User_Extension_Form.cleaned_data.get('fullname')
            # print('您输入的注册信息：',username,password,email,telephone,phone,fullname)
            user=User.objects.create_user(username=username, password=password,email=email)
            user.save()
            userextension=UserExtension.objects.create(telephone=telephone,phone=phone,fullname=fullname,user=user)
            userextension.save()
            return redirect(reverse('front:front_signin'))
        else:
            error_message1 =form.get_error()
            error_message2 =User_Extension_Form.get_error()
            # print('最终获得的错误信息：',{**error_message1,**error_message2})
            request.META['check_login_errors'] ={**error_message1,**error_message2}

    return render(request, generalVar.signup_url,{'obj':form,'obj2':User_Extension_Form})

@login_required
@require_http_methods(["GET","POST"])
def user_Show_Information(request):
    # userinformations = UserExtension.objects.get(user=request.user) if hasattr(request.user,'userinformations') else UserExtension.objects.create(user=request.user)

    front_user_extension = UserExtension.objects.get(user=request.user)
    department=set()
    position=set()
    for user_extension in UserExtension.objects.filter(user=request.user):
        for position_list in user_extension.position.values():
            # print(position_list)
            de=Department.objects.get(pk=position_list.get('department_id')).departmentName
            position.add('%s-%s'%(de,position_list.get('position')))
            department.add(de)
    department=','.join(list(department))
    position=','.join(list(position))
    return render(request, generalVar.user_Show_url,{'position':position,'department':department})


@login_required
@require_http_methods(["GET","POST"])
@csrf_exempt
def user_Edit_Information(request):
    front_user_extension = UserExtension.objects.get(user=request.user)
    department=set()
    position=set()
    for user_extension in UserExtension.objects.filter(user=request.user):
        for position_list in user_extension.position.values():
            # print(position_list)
            de=Department.objects.get(pk=position_list.get('department_id')).departmentName
            position.add('%s-%s'%(de,position_list.get('position')))
            department.add(de)
    department=','.join(list(department))
    position=','.join(list(position))
    extension_Form = User_Extension_Edit_Form(initial={
                "username":request.user.username,
                "email":request.user.email,
                "telephone":front_user_extension.telephone,
                "phone":front_user_extension.phone,
                "fullname":front_user_extension.fullname,
                "school":front_user_extension.school,
                "profession":front_user_extension.profession,
                "aboutme":front_user_extension.aboutme,
                "address":front_user_extension.address,
            })
    if request.method == 'POST':
        extension_Form = User_Extension_Edit_Form(request.POST)
        if extension_Form.is_valid():
            username = request.user.username
            email = extension_Form.cleaned_data.get('email')
            telephone = extension_Form.cleaned_data.get('telephone')
            phone = extension_Form.cleaned_data.get('phone')
            fullname = extension_Form.cleaned_data.get('fullname')
            school = extension_Form.cleaned_data.get('school')
            profession = extension_Form.cleaned_data.get('profession')
            aboutme = extension_Form.cleaned_data.get('aboutme')
            address = extension_Form.cleaned_data.get('address')
            myuser=User.objects.get(username=username)
            myuser.email=email
            myuser.save()
            userextension=UserExtension.objects.get(user=myuser)
            userextension.telephone=telephone
            userextension.phone=phone
            userextension.fullname=fullname
            userextension.school=school
            userextension.profession=profession
            userextension.aboutme=aboutme
            userextension.address=address
            userextension.save()
            return redirect(reverse('front:user_Show_Information'))
        else:
            extension_Form_return=User_Extension_Edit_Form(initial={
                "username":request.user.username,
                "email":request.POST.get('email'),
                "telephone":request.POST.get('telephone'),
                "phone":request.POST.get('phone'),
                "fullname":request.POST.get('fullname'),
                "school":request.POST.get('school'),
                "profession":request.POST.get('profession'),
                "aboutme":request.POST.get('aboutme'),
                "address":request.POST.get('address'),
            })
            request.META['check_login_errors'] =extension_Form_return.get_error()
            # print(extension_Form.errors.get_json_data())
            return render(request, generalVar.user_Edit_url, {'obj': extension_Form_return,'position':position,'department':department})

    return render(request, generalVar.user_Edit_url,{'obj':extension_Form,'position':position,'department':department})


@login_required()
@require_http_methods(["GET","POST"])
@csrf_exempt
def change_password(request):
    form = Change_Password_Form(request.POST)
    username = request.user.username
    fullname=request.user.extension.fullname
    if request.method == 'POST':
        if form.is_valid():
            password_old = form.cleaned_data.get('password_old')
            password_new = form.cleaned_data.get('password_new')
            myuser = authenticate(request, username=username, password=password_old)
            if myuser:
                myuser.set_password(password_new)
                myuser.save()
                logout(request)
                return redirect(reverse('front:front_signin'))
            else:
                request.META['check_login_errors'] = {
                    'password_old': [
                        ('验证错误：', '您的密码有误！')
                    ]
                }
        else:
            request.META['check_login_errors'] = form.get_error()

    return render(request, generalVar.change_password_url,{'obj':form,'username':username,'fullname':fullname})


@login_required()
@require_http_methods(["GET","POST"])
@csrf_exempt
def reset_password(request):
    form = Reset_Password_Form(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password_new = form.cleaned_data.get('password_new')
            # myuser = authenticate(username=username)
            myuser=User.objects.get(username=username)
            if myuser:
                myuser.set_password(password_new)
                myuser.save()
                # return redirect(reverse('front:front_signin'))
                request.META['check_login_errors'] = {
                    'success': [
                        (myuser.extension.fullname + '：', '的密码重置为' + password_new)
                    ]
                }
            else:
                request.META['check_login_errors'] = {
                    'username': [
                        ('验证错误：', '您的用户名有误！')
                    ]
                }
        else:
            request.META['check_login_errors'] = form.get_error()

    return render(request, generalVar.reset_password_url,{'obj':form})

@login_required()
@require_http_methods(['GET','POST'])
@csrf_exempt
def my_image(request):
    if request.method == 'POST':
        img = request.POST.get('img')
        userinfo = UserExtension.objects.get(user=request.user)
        userinfo.photo = img
        userinfo.save()
        return HttpResponse("1")
    else:
        return render(request, "Front/imagecrop.html")

@require_GET
def my_logout(request):
    logout(request)
    return redirect(reverse('front:front_index'))