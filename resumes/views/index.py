from .libraries import *


@login_required
def index_view(request):
    user = request.user
    if user.job_profile.full_name == "":
        messages.add_message(
            request, messages.INFO, "This needs to be completed before you continue!"
        )
        return redirect("resumes:user_job_profile", user.pk)

    user = request.user
    resumes = Resume.objects.order_by("-uploaded_on").filter(user_id=request.user)
    text = Pagetext.objects.get(pk=1)

    form = ResumeForm(request.POST, request.FILES)
    context = {"form": form, "user": user, "resumes": resumes, "text": text}
    load_context = {"user": user, "resumes": resumes, "text": text}
    if request.method == "POST":
        if form.is_valid():
            form.instance.user_id = request.user
            wait_for_doctype = form.save(commit=False)
            file_extension = pathlib.Path(str(wait_for_doctype.resume_path)).suffix

            if file_extension == ".txt" or file_extension == ".pdf":
                wait_for_doctype.save()
                messages.add_message(
                    request, messages.INFO, "Resume uploaded and ready to go!"
                )
                return redirect("resumes:index")
            else:
                messages.add_message(
                    request,
                    messages.INFO,
                    "Document type not supported, its gotta be a PDF.",
                )
                return redirect("resumes:index")
        else:
            form = ResumeForm()
            return render(request, "resumes/index.html", context)

    return render(request, "resumes/index.html", context=load_context)
