from BasicData.models import BasicData
from django.db import connection
from django.contrib.auth.models import User

abc1={
    'password': [
        {
            'message':'这个字段是必填项。',
            'code': 'required'
        }
    ]
}
def get_error_message_from_server():
    error_messages={}
    error_info = BasicData.objects.filter(groupName='验证错误信息').values_list()

    for QuerySetValue in error_info:
        itemName=QuerySetValue[3] #username
        itemYkey=QuerySetValue[5] #required
        itemValue1=QuerySetValue[6] #'必填项：'
        itemValue2=QuerySetValue[7] #'请输入用户名！'

        # 判断是否有重复的验证错误，比如username的required和max_length的itemName都是username，如果不这样获取itemName
        # 将会出现只保留required和max_length其中的一个
        if itemName in error_messages.keys():
            error_messages_dict=error_messages[itemName]
        else:
            error_messages_dict = {}

        error_messages_dict[itemYkey+'_translated']=itemValue1
        error_messages_dict[itemYkey]=itemValue2
        error_messages[itemName]=error_messages_dict

        # 创建如下字典
        # error_messages = {
        #     'username': {
        #         'required': '请输入用户名！',
        #         'required_translated': '必填项：',
        #         'max_length': '最大允许输入150个字符！',
        #         'max_length_translated': '超出限制：',
        #     },
        # }
    # print('传递前的error_messages',error_messages)
    return error_messages

def make_error_info(errors):
    new_errors = {}
    # print(errors)
    # print('转换前错误信息：',errors)
    error_messages=get_error_message_from_server()
    # print('转换后错误信息：',error_messages)

    for error_code, messages in errors.items():
        for error_code_set in messages:
            print('error_code:',error_code)
            print('error_code_set:',error_code_set)
            try :
                tmp_value = error_messages.get(error_code).get(error_code_set.get('code'))
            except :
                BasicData.objects.create(groupName='验证错误信息',projectName=error_code,projectDict=error_code_set.get('code'),projectKey=error_code_set.get('code'),projectValue=error_code_set.get('message'),lastEditName=User.objects.get(username='adminuser'),createName=User.objects.get(username='adminuser'))
                error_messages=get_error_message_from_server()
                print("执行了插入错误信息！")
            tmp_key = error_messages.get(error_code).get(error_code_set.get('code') + '_translated')
            tmp_value = error_messages.get(error_code).get(error_code_set.get('code'))
            new_errors[error_code] = [(tmp_key, tmp_value), ]

    # 遍历errors，在error_messages中查找错误值
    # 创建如下的效果：
    # new_errors={
    #     'password':[
    #         ('必填项：', '请输入密码！'),
    #         ('超出限制：', '最大允许输入128个字符！')
    #     ],
    #     'username':[
    #         ('必填项：', '请输入密码！'),
    #         ('超出限制：', '最大允许输入150个字符！')
    #     ]
    # }
    # print('最终效果：', new_errors)
    # print('sql查询次数：',len(connection.queries))
    return new_errors