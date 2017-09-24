from django import forms
from firstapp.models import FileModel

class UploadFileForm(forms.Form):
    number = forms.CharField()
    file = forms.FileField()
#    class Meta:
#        model = FileModel
#        fields = ['file_obj']
