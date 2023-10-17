from django import forms
from .models import Trip, TripComment


class CommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._widget_update()

    class Meta:
        model = TripComment
        fields = ["trip_comment_content"]

    def _widget_update(self):
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


# class BoardForm(forms.ModelForm):

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self._widget_update()

#     class Meta:
#         model = Trip
#         # fields = ["trip_name", "trip_category_detail", "trip_address", "trip_phone", "trip_time", "trip_homepage"]
#         # widgets = {
#         #     'trip_name': forms.TextInput(
#         #         attrs={
#         #             'placeholder': "가게 이름을 입력해주세요."
#         #         }
#         #     ),
#         #     'trip_category_detail': forms.TextInput(
#         #         attrs={
#         #             'placeholder': "카테고리를 입력해주세요."
#         #         }
#         #     ),
#         #     'trip_address': forms.TextInput(
#         #         attrs={
#         #             'placeholder': "주소를 입력해주세요."
#         #         }
#         #     ),
#         #     'trip_phone': forms.TextInput(
#         #         attrs={
#         #             'placeholder': "전화번호를 입력해주세요."
#         #         }
#         #     ),
#         #     'trip_time': forms.TextInput(
#         #         attrs={
#         #             'placeholder': "영업시간을 입력해주세요."
#         #         }
#         #     ),
#         #     'trip_homepage': forms.TextInput(
#         #         attrs={
#         #             'placeholder': "홈페이지 주소를 입력해주세요."
#         #         }
#         #     )
            
#         # }

#     def _widget_update(self):
#         for visible in self.visible_fields():
#             visible.field.widget.attrs['class'] = 'form-control'