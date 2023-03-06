from django import forms


class CommentForm(forms.Form):
    name = forms.CharField(
        max_length=60,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Your Name"
        })
    )
    feedback = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "Leave a comment!"
        })
    )
# class Add_Product_Form(forms.Form):
#     name = forms.CharField(
#         max_length=60,
#         widget=forms.TextInput(attrs={
#             "class": "form-control",
#             "placeholder": "Your Name"
#         })
#     )
#     feedback = forms.CharField(widget=forms.Textarea(
#         attrs={
#             "class": "form-control",
#             "placeholder": "Leave a comment!"
#         })
#     )