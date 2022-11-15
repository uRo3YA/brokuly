from django import forms
from .models import Product

#
class AddProductForm(forms.Form):
    quantity = forms.IntegerField()
    is_update = forms.BooleanField(
        required=False, initial=False, widget=forms.HiddenInput
    )


class ProductForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields["title"].label = "제품명"
        self.fields["title"].widget.attrs.update(
            {
                "placeholder": "제품명을 입력해주세요",
                "class": "form-control",
                "id": "form_title",
                "autofocus": True,
                "style": "width: 91%;",
            }
        )
        self.fields["price"].label = "가격"
        self.fields["price"].widget.attrs.update(
            {
                "placeholder": "가격을 입력해주세요",
                "class": "form-control",
                "id": "form_title",
                "style": "width: 91%;",
            }
        )
        self.fields["description"].label = "제품 설명"
        self.fields["description"].widget.attrs.update(
            {
                "placeholder": "제품 설명을 입력해주세요",
                "class": "form-control",
                "id": "form_title",
                "style": "width: 91%;",
            }
        )
        self.fields["stock"].label = "재고"
        self.fields["stock"].widget.attrs.update(
            {
                "placeholder": "재고를 입력해주세요",
                "class": "form-control",
                "id": "form_title",
                "style": "width: 91%;",
            }
        )
        self.fields["sales_rate"].label = "할인율"
        self.fields["sales_rate"].widget.attrs.update(
            {
                "placeholder": "할인율을 입력해주세요 (예: 10%)",
                "class": "form-control",
                "id": "form_title",
                "style": "width: 91%;",
            }
        )
        self.fields["produt_thum_img"].label = "상품 대표 사진"
        self.fields["produt_thum_img"].widget.attrs.update(
            {
                "placeholder": "상품 대표 사진을 업로드 해주세요",
                "class": "form-control",
                "id": "form_produt_thum_img",
                "style": "width: 91%;",
            }
        )
        self.fields["produt_detail_img"].label = "상품 상세 사진"
        self.fields["produt_detail_img"].widget.attrs.update(
            {
                "placeholder": "상품 대표 사진을 업로드 해주세요",
                "class": "form-control",
                "id": "form_produt_detail_img",
                "style": "width: 91%;",
            }
        )
        self.fields["produt_desc_img"].label = "성분 사진"
        self.fields["produt_desc_img"].widget.attrs.update(
            {
                "placeholder": "상품 성분 사진을 업로드 해주세요",
                "class": "form-control",
                "id": "form_produt_desc_img",
                "style": "width: 91%;",
            }
        )
        self.fields["allergy"].label = "알러지 정보"
        self.fields["allergy"].widget.attrs.update(
            {
                "placeholder": "알러지 정보를 선택해주세요",
                "class": "form-control",
                "id": "form_allergy",
                "style": "width: 91%;",
            }
        )
        self.fields["unit"].label = "단위"
        self.fields["unit"].widget.attrs.update(
            {
                "placeholder": "판매 단위를 입력해주세요 (예: 1kg/개)",
                "class": "form-control",
                "id": "form_unit",
                "style": "width: 91%;",
            }
        )
        self.fields["weight"].label = "중량"
        self.fields["weight"].widget.attrs.update(
            {
                "placeholder": "중량을 입력해주세요 (예: 1kg 또는 300g)",
                "class": "form-control",
                "id": "form_unit",
                "style": "width: 91%;",
            }
        )

    class Meta:
        model = Product
        fields = [
            "title",
            "price",
            "unit",
            "weight",
            "description",
            "stock",
            "sales_rate",
            "produt_thum_img",
            "produt_detail_img",
            "produt_desc_img",
            "allergy",
        ]
