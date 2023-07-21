from .models import Resume, CoverLetter, PdfContent, UserJobProfile
from django import forms


class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ("description", "resume_path")


class CoverLetterForm(forms.ModelForm):
    class Meta:
        model = CoverLetter
        fields = (
            "description_text",
            "job_description_url",
            "company_name",
            "show_company_name_on_pdf",
        )
        labels = {
            "description_text": "",
            "job_description_url": "Job description URL -- for your reference (optional)",
            "person": "Hiring Manager | Job Contact (optional)",
            "company_name": "Company (required)",
            "show_company_name_on_pdf": "show the company name on pdf?  |  if not selected, you can add it in the text area below",
            "content": "This is the 'addressed to' section of the letter. Include the contact person's name, title, company name, company address and any other info you like.",
        }


class EditCoverLetterForm(forms.ModelForm):
    class Meta:
        model = CoverLetter
        fields = (
            "content",
            "show_company_name_on_pdf",

        )
        labels = {
            "content": "This is the 'addressed to' section of the letter. Include the contact person's name, title, company name, company address and any other info you like.",
            "show_company_name_on_pdf": "show the company name on pdf?",
        }


class UserJobProfileForm(forms.ModelForm):
    class Meta:
        model = UserJobProfile
        fields = (
            "full_name",
            "show_my_name_on_pdf",
            "content",
        )
        labels = {
            "full_name": "Enter your full name",
            "show_my_name_on_pdf": "Show my name pn the PDF? | You can add your name to the heading content below",
            "content": "",
        }


class UserJobProfileNameForm(forms.ModelForm):
    class Meta:
        model = UserJobProfile
        fields = ("full_name",)
        labels = {
            "full_name": "Enter your full name",
        }


class EditGeneratedTextForm(forms.ModelForm):
    class Meta:
        model = PdfContent
        fields = ("llm_text",)
        labels = {
            "llm_text": "",
        }
