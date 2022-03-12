from django import forms


class UploadVideoForm(forms.Form):
    video = forms.FileField(label='Video')
    title = forms.CharField(max_length=255)
    tags = forms.CharField(label='Point tags', max_length=255)


