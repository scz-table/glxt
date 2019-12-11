from django import forms
from django.contrib.auth import get_user_model
# from django.contrib.auth.models import User
from User_Extension.models import UserExtension
from Universalscript import errorTips,generalVar


class SignupForm(forms.ModelForm):
    password_repeated = forms.CharField(
        max_length=120,
        label="验证密码",
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': '请再一次输入密码',
            }
            ,render_value=True))
    email = forms.EmailField(
        max_length=120,
        label="邮箱",
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': '请输入邮箱',
            }
            ))

    def clean_password_repeated(self):
        # cleaned_data=super(SignupForm,self).clean()
        password=self.cleaned_data.get('password')
        password_repeated=self.cleaned_data.get('password_repeated')
        # print(password_repeated,'   ',password)
        if password != password_repeated:
            raise forms.ValidationError(message='两侧密码输入不一致！')
        return self.cleaned_data
    class Meta:
        model = get_user_model()
        fields =['password','username']
        widgets = {
            'username': forms.TextInput(attrs={
                                    'class': 'form-control',
                                    'placeholder': '请输入工作证号',
                                    }),
            'password': forms.PasswordInput(attrs={
                                    'class': 'form-control',
                                    'placeholder': '请输入密码',
                                    }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['email'].widget.attrs.update({'class': 'form-control form-control1'})

    def get_error(self):
        # print('验证表单出现的错误：',self.errors.get_json_data())
        return errorTips.make_error_info(self.errors.get_json_data())

class User_Extension_Signup_Form(forms.ModelForm):

    class Meta:
        model=UserExtension
        fields=["fullname","telephone","phone"]
        widgets = {
            'fullname': forms.TextInput(attrs={
                                    'class': 'form-control',
                                    'placeholder': '请输入真实姓名用于验证',
                                    }),
            'telephone': forms.TextInput(attrs={
                                    'class': 'form-control',
                                    'placeholder': '请输入手机号码',
                                    }),
            'phone': forms.TextInput(attrs={
                                    'class': 'form-control',
                                    'placeholder': '请输入座机号码',
                                    }),
        }
    def get_error(self):
        # print('验证表单出现的错误：',self.errors.get_json_data())
        return errorTips.make_error_info(self.errors.get_json_data())

class SigninForm(forms.Form):
    username =forms.CharField(
        max_length=150,
        label="工作证号",
        widget=forms.TextInput(attrs={
            'class': 'layui-input',
            'placeholder': '请输入工作证号',
            'lay-verify':"required",
            'autocomplete':"off",
            'id':"username",
        }),
    )
    # username.widget.attrs.update({'class': 'special'})
    password =forms.CharField(
        max_length=120,
        label="密码",
        widget=forms.PasswordInput(
            attrs={
                'class': 'layui-input',
                'placeholder': '请输入密码',
                'lay-verify':"required|password",
                'autocomplete':"off",
                'id':"password",
            }
            ,render_value=True))
    # remember =forms.ChoiceField(
    #     required=False,
    #     label="记住密码",
    #     initial="checked",
    #     choices=((0, 'False'), (1, 'True'),(0, False), (1, True), (1, 'on')),
    #     widget=forms.widgets.CheckboxInput(
    #
    #         attrs={
    #             'class': 'control-lable',
    #         }
    #     )
    # )
    def get_error(self):
        return errorTips.make_error_info(self.errors.get_json_data())


class Change_Password_Form(forms.Form):

    password_old = forms.CharField(
        max_length=120,
        label="旧密码",
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': '请输入旧密码',
            }
            ,render_value=True))
    password_new = forms.CharField(
        max_length=120,
        label="新密码",
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': '请输入新密码',
            }
            ,render_value=True))
    password_repeated = forms.CharField(
        max_length=120,
        label="验证密码",
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': '请再一次输入密码',
            }
            ,render_value=True))

    def clean_password_repeated(self):
        # cleaned_data=super(Change_Password_Form,self).clean_password_repeated()
        password_new=self.cleaned_data.get('password_new')
        password_repeated=self.cleaned_data.get('password_repeated')
        if password_new != password_repeated:
            raise forms.ValidationError(message='两侧密码输入不一致！',code='notsame')
        return self.cleaned_data

    def get_error(self):
        return errorTips.make_error_info(self.errors.get_json_data())

class Reset_Password_Form(forms.Form):

    username =forms.CharField(
        max_length=150,
        label="用户名",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '请输入工作证号',
        }),
    )
    password_new = forms.CharField(
        max_length=120,
        label="新密码",
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': '请输入新密码',
            }
            ,render_value=True))
    def get_error(self):
        return errorTips.make_error_info(self.errors.get_json_data())

class User_Extension_Edit_Form(forms.ModelForm):

    username =forms.CharField(
        max_length=150,
        label="用户名",
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '该信息没有填写',
        }),
    )
    email = forms.EmailField(
        max_length=120,
        label="邮箱",
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': '请输入邮箱',
            }
            ))

    telephone = forms.CharField(
        max_length=11,
        label="手机",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '请输入手机号码',
            }
            ))

    position =forms.CharField(
        max_length=200,
        label="职位",
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '该信息没有填写',
        }),
    )
    department =forms.CharField(
        max_length=200,
        label="部门",
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '该信息没有填写',
        }),
    )
    class Meta:
        model=UserExtension
        fields=["fullname","phone","school","photo","profession","address","aboutme"]
        widgets = {
            'fullname': forms.TextInput(attrs={
                                    'class': 'form-control',
                                    'placeholder': '请输入真实姓名用于验证',
                                    }),
            'phone': forms.TextInput(attrs={
                                    'class': 'form-control',
                                    'placeholder': '请输入座机号码',
                                    }),
            'school': forms.TextInput(attrs={
                                    'class': 'form-control',
                                    'placeholder': '请输入学校',
                                    }),
            'profession': forms.TextInput(attrs={
                                    'class': 'form-control',
                                    'placeholder': '请输入专业',
                                    }),
            'address': forms.TextInput(attrs={
                                    'class': 'form-control',
                                    'placeholder': '请输入居住住址',
                                    }),
            'aboutme': forms.TextInput(attrs={
                                    'class': 'form-control',
                                    'placeholder': '请输入自我介绍',
                                    }),
        }
    def get_error(self):
        # print('修改用户信息的错误信息：',self.errors.get_json_data())
        return errorTips.make_error_info(self.errors.get_json_data())