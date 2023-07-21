from .libraries import *

@login_required
def cover_address_view(request, pk, pdf_key):
    user = request.user
    # resume = Resume.objects.get(pk=pk)
    cover = CoverLetter.objects.get(pk=pk)
    pdf = PdfContent.objects.get(id=pdf_key)
    text = Pagetext.objects.get(pk=1)

    form = EditCoverLetterForm(request.POST or None, instance=cover)
    context = {
        "form": form,
        "user": user,
        "cover": cover,
        "text": text,
        # "resume": resume,
        "pdf": pdf,
    }
    load_context = {
        "form": form,
        "user": user,
        "cover": cover,
        "text": text,
        # "resume": resume,
        "pdf": pdf,
    }
    if user != cover.user_id:
        messages.add_message(request, messages.INFO, "Unauthorized Baby!")
        return redirect("/")
    else:
        if request.method == "POST":
            if form.is_valid():
                # form.instance.resume_id = resume
                form.instance.user_id = request.user

                wait_to_save = form.save(commit=False)

                wait_to_save.save()

                messages.add_message(request, messages.INFO, "Job company/manager info updated.")
                return redirect("resumes:pdf_html", pdf.id)
            else:
                messages.add_message(
                    request,
                    messages.INFO,
                    "Please complete all required fields to continue.",
                )
                return render(request, "resumes/cover_address_form.html", context)

    return render(request, "resumes/cover_address_form.html", context=load_context)
