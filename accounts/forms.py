from django.contrib.auth.forms import UserCreationForm, UserChangeForm,PasswordChangeForm
from django.contrib.auth import get_user_model
from django import forms

class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        
        self.fields["username"].label = "아이디"
        self.fields["username"].widget.attrs.update(
            {
                "placeholder": "아이디를 입력해주세요.",
                "class": "form-control mx-0",
                "style": "width: 100%; height: 50px;",
            }
        )

        self.fields["password1"].label = "비밀번호"
        self.fields["password1"].widget.attrs.update(
            {
                "placeholder": "비밀번호를 입력해주세요.",
                "class": "form-control",
                "style": "width: 100%; height: 50px;",
            }
        )

        self.fields["password2"].label = "비밀번호 확인"
        self.fields["password2"].widget.attrs.update(
            {
                "placeholder": "비밀번호를 한번 더 입력해주세요.",
                "class": "form-control",
                "style": "width: 100%; height: 50px;",
            }
        )

        self.fields["name"].label = "이름"
        self.fields["name"].widget.attrs.update(
            {
                "placeholder": "이름을 입력해주세요.",
                "class": "form-control",
                "style": "width: 100%; height: 50px;",
            }
        )       

        self.fields["email"].label = "이메일"
        self.fields["email"].widget.attrs.update(
            {
                "placeholder": "예 : brokurly@brokurly.com",
                "class": "form-control mx-0",
                "style": "width: 100%; height: 50px;",
            }
        )       

        self.fields["address"].label = "주소"
        self.fields["address"].widget.attrs.update(
            {
                "placeholder": "주소 검색",
                "class": "form-control",
                "style": "width: 100%; height: 50px;",
            }
        ) 
    class Meta:
        model = get_user_model()
        fields = ['username', 'password1', 'password2', 'name', 'email', 'address', ]


# 이름, 이메일, 주소 필드를 가져오려면
# 다중 상속을 할 수 밖에 없다.
class CustomUserChangeForm(PasswordChangeForm, UserChangeForm):
    def __init__(self, *args, **kwargs):
        super(CustomUserChangeForm, self).__init__(*args, **kwargs)
        
        self.fields["old_password"].label = ""
        self.fields["old_password"].widget.attrs.update(
            {
                "placeholder": "현재 비밀번호를 입력해주세요.",
                "class": "form-control",
                "style": "width: 100%; height: 50px;",
                "required": True,
            }
        )

        self.fields["new_password1"].label = ""
        self.fields["new_password1"].widget.attrs.update(
            {
                "placeholder": "새 비밀번호를 입력해주세요.",
                "class": "form-control",
                "style": "width: 100%; height: 50px;",
                "required": True,
            }
        )

        self.fields["new_password2"].label = ""
        self.fields["new_password2"].widget.attrs.update(
            {
                "placeholder": "새 비밀번호를 한번 더 입력해주세요.",
                "class": "form-control",
                "style": "width: 100%; height: 50px;",
                "required": True,
            }
        )

        self.fields["name"].label = ""
        self.fields["name"].widget.attrs.update(
            {
                "placeholder": "이름을 입력해주세요.",
                "class": "form-control",
                "style": "width: 100%; height: 50px;",
                "required": True,
            }
        )       

        self.fields["email"].label = ""
        self.fields["email"].widget.attrs.update(
            {
                "placeholder": "예 : brokurly@brokurly.com",
                "class": "form-control mx-0",
                "style": "width: 100%; height: 50px;",
                "required": True,
            }
        )       

        self.fields["address"].label = ""
        self.fields["address"].widget.attrs.update(
            {
                "placeholder": "주소 검색",
                "class": "form-control",
                "style": "width: 100%; height: 50px;",
                "required": True,
            }
        )
    
    
    # 데이터는 클라이언트로 부터 가져오지만
    # DB 에 저장하지 못한다. 
    # MRO : Method Resolution Order 때문인듯 하다.
    # link : https://engineer-mole.tistory.com/196
    def save(self):
        user = super().save(commit=True)

        # MRO 에 따라서 해결되지 않은 필드는 수작업으로 저장한다.
        user.name = self.cleaned_data['name']
        user.email = self.cleaned_data['email']
        user.address = self.cleaned_data['address']

        user.save()

        return self.user


    class Meta:
        model = get_user_model()
        fields = ['old_password', 'new_password1', 'new_password2', 'name', 'email', 'address']