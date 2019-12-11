from User_Extension.models import *
from django.contrib.auth.decorators import login_required,permission_required
from django.shortcuts import redirect,reverse,render


# @login_required(login_url='/signin/')
def front_user(request):
    # no_login_list=[
    #     reverse('front:front_signin'),
    #     reverse('front:front_signup'),
    # ]
    # if not request.path in no_login_list or not request.user.username:
    #     return redirect(reverse('front:front_index'))

    # print('上下文处理器得到的错误信息：',request.META.get('check_login_errors'))
    context={}
    context['check_login_errors'] = request.META.get('check_login_errors')
    if request.user:
        try:
            front_user=request.user
            front_user_extension=UserExtension.objects.get(user=front_user)
            front_user_permission=front_user.get_all_permissions()
            front_user_groups_permission=front_user.get_group_permissions()
            context['front_user']=front_user
            context['front_user_extension']=front_user_extension
            context['front_user_permission']=front_user_permission
            context['front_user_groups_permission']=front_user_groups_permission
            # print(front_user_groups_permission)
        except:
            pass
    return context