from .models import Document
from django import forms



class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'path_to_file' )
        # widgets = {'document_url': forms.HiddenInput()}
        # def __init__(self, *args, **kwargs):
        #     super(DocumentForm, self).__init__(*args, **kwargs)
        #     self.fields['document_url'].initial = self.document_path