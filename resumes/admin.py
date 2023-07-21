from django.contrib import admin
from .models import Resume, CoverLetter, UserJobProfile, PdfContent

admin.site.register([Resume, CoverLetter, UserJobProfile, PdfContent])
