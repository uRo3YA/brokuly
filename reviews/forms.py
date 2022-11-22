from django import forms
from .models import Review, Comment


class ReviewForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)
        self.fields["title"].label = "제목"
        self.fields["title"].widget.attrs.update(
            {
                "placeholder": "제목을 입력해주세요.",
                "class": "form-control",
                "id": "form_title",
                "autofocus": True,
            }
        )
        self.fields["grade"].label = "별점"
        self.fields["grade"].widget.attrs.update(
            {"class": "form-control", "autofocus": False, "style": "width: 40%; "}
        )
        self.fields["content"].label = "내용"
        self.fields["content"].widget.attrs.update(
            {
                "placeholder": "후기를 작성해주세요.",
                "class": "form-control",
                "id": "form_content",
                "autofocus": False,
            }
        )
        # self.fields["image"].label = "첨부 이미지"
        # self.fields["image"].widget.attrs.update(
        #     {"class": "form-control", "autofocus": False, "style": "width: 40%; "}
        # )

    class Meta:
        model = Review
        # fields = ["title", "grade", "content", "image"]
        fields = [
            "title",
            "grade",
            "content",
        ]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            "content",
        ]
