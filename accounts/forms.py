from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        
        self.fields["username"].label = "아이디"
        self.fields["username"].widget.attrs.update(
            {
                "placeholder": "아이디를 입력해주세요.",
                "class": "form-control mx-0",
                "style": "width: 100%;",
            }
        )

        self.fields["password1"].label = "비밀번호"
        self.fields["password1"].widget.attrs.update(
            {
                "placeholder": "비밀번호를 입력해주세요.",
                "class": "form-control",
                "style": "width: 100%;",
            }
        )

        self.fields["password2"].label = "비밀번호 확인"
        self.fields["password2"].widget.attrs.update(
            {
                "placeholder": "비밀번호를 한번 더 입력해주세요.",
                "class": "form-control",
                "style": "width: 100%;",
            }
        )

        self.fields["name"].label = "이름"
        self.fields["name"].widget.attrs.update(
            {
                "placeholder": "이름을 입력해주세요.",
                "class": "form-control",
                "style": "width: 100%;",
            }
        )       

        self.fields["email"].label = "이메일"
        self.fields["email"].widget.attrs.update(
            {
                "placeholder": "예 : brokurly@brokurly.com",
                "class": "form-control mx-0",
                "style": "width: 100%;",
            }
        )       

        self.fields["address"].label = "주소"
        self.fields["address"].widget.attrs.update(
            {
                "placeholder": "주소 검색",
                "class": "form-control",
                "style": "width: 100%;",
            }
        ) 
    class Meta:
        model = get_user_model()
        fields = ['username', 'password1', 'password2', 'name', 'email', 'address', ]