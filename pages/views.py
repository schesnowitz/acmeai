from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from documents.models import Session, Document
from pages.models import Profile, Pagetext
from chats.models import Chat, Instruction
from urls.models import Urlsession, Url
from pages.forms import ProfileForm
from django.contrib import messages
from resumes.models import Resume, CoverLetter, PdfContent

@login_required
def profile_view(request, pk):
    user = request.user
    profile = Profile.objects.get(id=pk)
    form = ProfileForm(request.POST or None, instance=profile)
    documents = Document.objects.filter(created_by=user)
    chats = Instruction.objects.filter(user_id=user)
    urls = Url.objects.filter(user_id=user)
    resumes = Resume.objects.filter(user_id=user)  
    cover_letters = PdfContent.objects.filter(user=user)
    text = Pagetext.objects.get(id=1)
    context = {
        "documents": documents,
        "chats": chats,
        "urls": urls,
        "form": form,
        "text": text,
        "resumes": resumes,
        "cover_letters": cover_letters,
    }
    if user != profile.user:
        messages.add_message(request, messages.INFO, "Unauthorized Baby!")
        return redirect('/')
    else:
        if request.method == "POST":
            if form.is_valid():
                form.save()
                messages.add_message(request, messages.INFO, "Your info has been saved")

                return redirect("pages:user_profile", profile.id)
            else:
                messages.add_message(
                    request,
                    messages.INFO,
                    "Try your request again, as there was a problem getting a response from the AI.",
                )
                return render(request, "pages/profile.html", context)
        return render(request, "pages/profile.html", context)


def index_view(request):
    text = Pagetext.objects.get(id=1)
    context = {"text": text}
    return render(request, "pages/index.html", context=context)

def private_view(request):
    text = Pagetext.objects.get(id=1)
    context = {"text": text}
    return render(request, "pages/private.html", context=context)