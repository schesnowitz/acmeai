from chats.models import Instruction, Chat
from django import forms



class InstructionForm(forms.ModelForm):
    class Meta:
        model = Instruction
        fields = ('description', 'prompt', 'data' )
        # widgets = {'document_url': forms.HiddenInput()}
        # def __init__(self, *args, **kwargs):
        #     super(DocumentForm, self).__init__(*args, **kwargs)
        #     self.fields['document_url'].initial = self.document_path

