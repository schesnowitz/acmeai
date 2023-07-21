from .libraries import *



@login_required
def create_cover_view(request, pk):
    user = request.user
    resume = Resume.objects.get(pk=pk)
    cover = CoverLetter.objects.order_by("-time").filter(resume_id=resume)
    text = Pagetext.objects.get(pk=1)
    form = CoverLetterForm(request.POST or None)
    context = {
        "form": form,
        "user": user,
        "cover": cover,
        "text": text,
        "resume": resume,
    }
    load_context = {
        "form": form,
        "user": user,
        "cover": cover,
        "text": text,
        "resume": resume,
    }
    if user != resume.user_id:
        messages.add_message(request, messages.INFO, "Unauthorized Baby!")
        return redirect("/")
    if request.method == "POST":
        if form.is_valid():
            form.instance.resume_id = resume
            form.instance.user_id = request.user
            wait_to_save = form.save(commit=False)
            wait_to_save.save()
            messages.add_message(request, messages.INFO, "Job description created")
            # return render(request, "resumes/create_content.html", context)
            return HttpResponseRedirect(reverse("resumes:create", args=(resume.id,)))
        else:
            messages.add_message(request, messages.INFO, "Please complete all required fields to continue.")
            return render(request, "resumes/create.html", context)

    return render(request, "resumes/create.html", context=load_context)
