from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from ..models import Resume, CoverLetter, PdfContent, UserJobProfile
from ..forms import (
    ResumeForm,
    CoverLetterForm,
    UserJobProfileForm,
    EditGeneratedTextForm,
    EditCoverLetterForm,
    UserJobProfileNameForm,
)
from pages.models import Pagetext
import pathlib
from ..functions import resume_cover_llm

import os
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders
from datetime import datetime
